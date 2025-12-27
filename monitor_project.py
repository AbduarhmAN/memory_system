"""
🔍 PROJECT MONITOR - Real-Time State Watcher (JSON Edition)
============================================================
This script runs in the background and watches for file changes.
When any status.md or Current_Focus.txt changes, it regenerates
the full project tree and writes it to PROJECT_MAP.json.

USAGE:
    pip install watchdog
    python monitor_project.py

The AI reads PROJECT_MAP.json to understand the full system state instantly.
"""

import os
import time
import json
from pathlib import Path

# Try to use watchdog (event-driven, efficient)
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    USE_WATCHDOG = True
except ImportError:
    USE_WATCHDOG = False
    print("[WARNING] watchdog not installed. Using 2-second polling instead.")
    print("[TIP] Run: pip install watchdog")


# ============================================================
# CONFIGURATION
# ============================================================
PROJECT_ROOT = Path(__file__).parent.resolve()
PROBLEMS_DIR = PROJECT_ROOT / "problems"
FOCUS_FILE = PROJECT_ROOT / "Current_Focus.txt"
OUTPUT_FILE = PROJECT_ROOT / "PROJECT_MAP.json"


# ============================================================
# CORE LOGIC: THE CRAWLER
# ============================================================
def read_focus_pointer():
    """Read the Current_Focus.txt file."""
    if FOCUS_FILE.exists():
        return FOCUS_FILE.read_text(encoding="utf-8").strip()
    return None

def read_status_file(folder_path):
    """Read status.md and return list of dicts: {'name': 'P1', 'status': '[*]' }"""
    status_file = folder_path / "status.md"
    items = []
    if status_file.exists():
        content = status_file.read_text(encoding="utf-8")
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("- ["):
                # Determine status
                if "[x]" in line:
                    status = "DONE"
                elif "[*]" in line:
                    status = "ACTIVE"
                else:
                    status = "PENDING"
                
                # Extract name
                try:
                    name_part = line.split("]")[1].strip()
                    name = name_part.split("(")[0].strip()
                    items.append({"name": name, "status": status})
                except:
                    pass
    return items

def crawl_folder_recursive(folder_path):
    """Recursively crawl and build a nested dict tree."""
    node_data = {
        "path": str(folder_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "status_file": read_status_file(folder_path),
        "sub_folders": {}
    }

    # Find actual directories
    sub_dir = folder_path / "sub"
    if sub_dir.exists():
        for child in sorted(sub_dir.iterdir()):
            if child.is_dir():
                node_data["sub_folders"][child.name] = crawl_folder_recursive(child)
    
    return node_data

def generate_full_state():
    """Generate the complete project state object."""
    state = {
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
        "project_root": str(PROJECT_ROOT),
        "current_focus_pointer": read_focus_pointer(),
        "tree": {},
        "validation": {
            "errors": [],
            "warnings": [],
            "active_pointers": []
        }
    }

    # Crawl Problems
    if PROBLEMS_DIR.exists():
        for problem_folder in sorted(PROBLEMS_DIR.iterdir()):
            if problem_folder.is_dir():
                state["tree"][problem_folder.name] = crawl_folder_recursive(problem_folder)
    
    # -------------------------------------------------
    # VALIDATION LOGIC
    # -------------------------------------------------
    
    # 1. Gather all active pointers
    def find_active(node):
        for item in node.get("status_file", []):
            if item["status"] == "ACTIVE":
                state["validation"]["active_pointers"].append(
                    f"{node['path']}/{item['name']}"
                )
        for sub in node.get("sub_folders", {}).values():
            find_active(sub)

    for p_node in state["tree"].values():
        find_active(p_node)

    # 2. Check Active Count
    count = len(state["validation"]["active_pointers"])
    if count == 0:
        state["validation"]["warnings"].append("No active [*] pointer found in any status.md")
    elif count > 1:
        state["validation"]["errors"].append(f"Multiple active pointers detected: {state['validation']['active_pointers']}")

    # 3. Check Pointer File Alignment
    pointer = state["current_focus_pointer"]
    if pointer:
        # Check if path exists
        full_path = PROJECT_ROOT / pointer
        if not full_path.exists():
             state["validation"]["errors"].append(f"Current_Focus.txt points to non-existent path: {pointer}")
    else:
        state["validation"]["warnings"].append("Current_Focus.txt is empty or missing")

    return state

def write_output():
    """Generate state and write JSON."""
    try:
        state = generate_full_state()
        json_str = json.dumps(state, indent=2)
        OUTPUT_FILE.write_text(json_str, encoding="utf-8")
        print(f"[{time.strftime('%H:%M:%S')}] PROJECT_MAP.json updated.")
    except Exception as e:
        print(f"[ERROR] Failed to update: {e}")

# ============================================================
# WATCHER MODE
# ============================================================
if USE_WATCHDOG:
    class ProjectChangeHandler(FileSystemEventHandler):
        def __init__(self):
            self.last_update = 0
            self.debounce = 0.5
        
        def on_any_event(self, event):
            if event.is_directory: return
            src = str(event.src_path)
            if "status.md" in src or "Current_Focus.txt" in src:
                now = time.time()
                if now - self.last_update > self.debounce:
                    self.last_update = now
                    write_output()

    def run_watchdog_mode():
        print(f"[WATCHDOG] MODE ACTIVE. Watching: {PROJECT_ROOT}")
        print(f"[OUTPUT] File: {OUTPUT_FILE}")
        write_output()
        observer = Observer()
        observer.schedule(ProjectChangeHandler(), str(PROJECT_ROOT), recursive=True)
        observer.start()
        try:
            while True: time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
else:
    def run_watchdog_mode():
        # Fallback - shouldn't be called
        run_polling_mode()

def run_polling_mode():
    import sys
    if sys.platform == "win32":
        # Fix Windows console encoding
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    print(f"⚠️ POLLING MODE (Fallback). Watching: {PROJECT_ROOT}")
    write_output()
    last_hash = ""
    try:
        while True:
            # We must re-generate to check for changes if we aren't using file events
            # This is less efficient but necessary for fallback
            state = generate_full_state()
            new_hash = str(state) # simple content hash
            if new_hash != last_hash:
                json_str = json.dumps(state, indent=2)
                OUTPUT_FILE.write_text(json_str, encoding="utf-8")
                print(f"[{time.strftime('%H:%M:%S')}] PROJECT_MAP.json updated.")
                last_hash = new_hash
            time.sleep(2)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    if USE_WATCHDOG:
        run_watchdog_mode()
    else:
        run_polling_mode()
