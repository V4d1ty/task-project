DEFAULT_PRIORITY = "high"  #вариант Б

# код
def add_task(title, priority=DEFAULT_PRIORITY):
    if not title:
        raise ValueError("Title cannot be empty")
    return {"title": title, "status": "open", "priority": priority}

def mark_done(task):
    task["status"] = "done"

def filter_tasks(tasks, status):
    return [t for t in tasks if t["status"] == status]

def sort_tasks_by_priority(tasks):
    order = {"high": 0, "normal": 1, "low": 2}
    return sorted(tasks, key=lambda t: order.get(t.get("priority", "normal"), 1))

def main():
    print("Task App started")

if __name__ == "__main__":
    main()