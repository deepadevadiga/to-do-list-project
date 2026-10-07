import json
from pathlib import Path

FILE = Path("todos.json")

def load():
    return json.loads(FILE.read_text()) if FILE.exists() else []

def save(items):
    FILE.write_text(json.dumps(items, indent=2))

def main():
    todos = load()
    while True:
        print("\n1.Add  2.List  3.Complete  4.Delete  5.Exit")
        choice = input("> ")
        if choice == "1":
            todos.append({"task": input("Task: "), "done": False})
            save(todos)
        elif choice == "2":
            for i, t in enumerate(todos, 1):
                print(f"{i}. [{'x' if t['done'] else ' '}] {t['task']}")
        elif choice == "3":
            try: todos[int(input("Number: "))-1]["done"] = True; save(todos)
            except (ValueError, IndexError): print("Invalid number.")
        elif choice == "4":
            try: todos.pop(int(input("Number: "))-1); save(todos)
            except (ValueError, IndexError): print("Invalid number.")
        elif choice == "5": break

if __name__ == "__main__": main()
