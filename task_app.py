import json
import os
import sys
import pathlib
from http.server import BaseHTTPRequestHandler, HTTPServer

TASKS_FILE = "tasks.json"
DEFAULT_PRIORITY = "normal"

def load_tasks(file_path=TASKS_FILE):
    if not os.path.exists(file_path):
        return [
            {"id": 1, "title": "Task 1", "status": "open", "priority": "normal"},
            {"id": 2, "title": "Task 2", "status": "done", "priority": "high"}
        ]
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def increment_counter():
    path = pathlib.Path("/data/state.json")
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"requests": 0}
    data["requests"] += 1
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)

class TaskHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        increment_counter()
        if self.path == "/tasks":
            tasks = load_tasks()
            version = os.environ.get("APP_VERSION", "unknown")
            response = {"tasks": tasks, "version": version}
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode("utf-8"))
        elif self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass 

def run_server():
    port = int(os.environ.get("PORT", "8001"))
    message = os.environ.get("MESSAGE", "Service online")
    print(f"{message} on port {port}")
    server = HTTPServer(("0.0.0.0", port), TaskHandler)
    server.serve_forever()

def main():
    print("Task App started")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        run_server()
    else:
        main()