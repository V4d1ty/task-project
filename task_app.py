def add_task(title):
    if not title:
        raise ValueError("Title cannot be empty")
    return {"title": title, "status": "open"}

def main():
    print("Task App started")

if __name__ == "__main__":
    main()