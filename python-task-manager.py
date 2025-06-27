from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Task:
    title: str
    duration: int
    priority: int

def insert(queue: List[Task], task: Task) -> None:
    queue.append(task)

def is_empty(queue: List[Task]) -> bool:
    return len(queue) == 0

def peek(queue: List[Task]) -> Optional[Task]:
    return queue[0] if not is_empty(queue) else None

def extract(queue: List[Task]) -> Optional[Task]:
    return queue.pop(0) if not is_empty(queue) else None

def complete_next_task(queue: List[Task]) -> Optional[Task]:
    if is_empty(queue):
        print("No tasks to complete.")
        return None
    best = min(queue, key=lambda t: t.priority)
    print(f"Completing task: {best.title} (duration: {best.duration} min, priority: {best.priority})")
    queue.remove(best)
    return best

def sort_tasks(queue: List[Task], descending: bool = False) -> List[Task]:
    return sorted(queue, key=lambda t: t.duration, reverse=descending)

def search_for_task(queue: List[Task], title: str) -> Optional[int]:
    sorted_q = sorted(queue, key=lambda t: t.title)
    lo, hi = 0, len(sorted_q) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_q[mid].title == title:
            return mid
        if sorted_q[mid].title < title:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

def main():
    queue: List[Task] = []
    n = int(input("How many tasks? "))
    for i in range(n):
        print(f"Task #{i+1}")
        title    = input("  Title: ")
        duration = int(input("  Duration (mins): "))
        priority = int(input("  Priority (lower value = higher): "))
        insert(queue, Task(title, duration, priority))

    menu = """
MENU
1) Peek next task
2) Extract next task
3) Complete next task
4) Sort tasks by duration
5) Search for a task
6) Show all tasks
0) Exit
> """

    while True:
        choice = input(menu).strip()
        if choice == "1":
            t = peek(queue)
            print("Next task:", t)
        elif choice == "2":
            t = extract(queue)
            print("Extracted:", t)
        elif choice == "3":
            complete_next_task(queue)
        elif choice == "4":
            order = input("Sort ascending or descending? (a/d): ").lower()
            sorted_q = sort_tasks(queue, descending=(order == "d"))
            print("Sorted tasks:")
            for t in sorted_q:
                print(" ", t)
        elif choice == "5":
            title = input("Title to search: ")
            idx = search_for_task(queue, title)
            if idx is not None:
                print(f"Found '{title}' at index {idx}.")
            else:
                print("Task not found.")
        elif choice == "6":
            print("All tasks:")
            for t in queue:
                print(" ", t)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
