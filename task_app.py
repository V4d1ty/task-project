DEFAULT_PRIORITY = "normal"

def add_task(title, priority=DEFAULT_PRIORITY):
    if not title:
        raise ValueError("Title cannot be empty")
    return {"title": title, "status": "open", "priority": priority}

def mark_done(task):
    task["status"] = "done"

def filter_tasks(tasks, status):
    return [t for t in tasks if t["status"] == status]

def main():
    print("Task App started")

if __name__ == "__main__":
    main()