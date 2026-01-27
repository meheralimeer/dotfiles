#!/usr/bin/env python3

import json
import subprocess
import sys

def get_windows():
    try:
        # Get all clients in JSON format
        cmd = ["hyprctl", "clients", "-j"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        clients = json.loads(result.stdout)
        
        # Get active workspace ID
        cmd_active = ["hyprctl", "activeworkspace", "-j"]
        result_active = subprocess.run(cmd_active, capture_output=True, text=True, check=True)
        active_ws = json.loads(result_active.stdout)
        active_ws_id = active_ws['id']
        
        current_ws_clients = [c for c in clients if c['workspace']['id'] == active_ws_id]
        
        # Find active window to display as text
        active_client = next((c for c in current_ws_clients if c['focusHistoryID'] == 0), None)
        
        # Fallback if focusHistoryID logic isn't perfect or needed, just use 'title' from activewindow
        # specific to the currently focused window
        cmd_active_win = ["hyprctl", "activewindow", "-j"]
        result_win = subprocess.run(cmd_active_win, capture_output=True, text=True)
        active_window_title = "..."
        if result_win.returncode == 0 and result_win.stdout.strip() != "{}": # Check for empty json
             try:
                active_win_data = json.loads(result_win.stdout)
                active_window_title = active_win_data.get('title', "Desktop")
             except:
                pass
        else:
             active_window_title = "Desktop"

        # Build tooltip
        tooltip_lines = []
        for client in current_ws_clients:
            title = client['title']
            # Escape strings if necessary
            tooltip_lines.append(f"• {title}")
            
        tooltip = "\n".join(tooltip_lines)
        if not tooltip:
            tooltip = "No windows"

        # Output JSON for Waybar
        output = {
            "text": active_window_title if len(active_window_title) < 40 else active_window_title[:40] + "...",
            "tooltip": tooltip,
            "class": "custom-windows",
            "alt": "windows"
        }
        
        print(json.dumps(output))
        
    except Exception as e:
        print(json.dumps({"text": "Error", "tooltip": str(e)}))

if __name__ == "__main__":
    get_windows()
