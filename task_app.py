def add_task(title):
    if not title:
        raise ValueError("Title cannot be empty")
    return {"title": title, "status": "open"}

def mark_done(task):
    task["status"] = "done"

def filter_tasks(tasks, status):
    return [t for t in tasks if t["status"] == status]

def main():
    print("Task App started")

if __name__ == "__main__":
    main()