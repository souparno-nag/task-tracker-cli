import os
import sys
import json
# from dataclasses import dataclass, asdict
import pprint

FILEPATH = 'tasks.json'

# Check if the file exists
if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as f:
        json.dump({}, f)
    print(f"{FILEPATH} created.")
else:
    print(f"{FILEPATH} already exists.")
    
#list of commands
commands = ["add", "update", "delete", "mark-in-progress", "mark-done", "list", "list-todo", "list-in-progress", "list-done"]

argv = sys.argv
# print(argv)

class Task:
    id: int
    description: str
    status: str
    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status
        # self.createdAt = createdAt
        # self.updatedAt = updatedAt
        
# sen = argv[1:].join(' ')
# sen = ' '.join(a for a in argv[1:])
# print(sen)

FILEPATH = 'tasks.json'
# def get_json_data():
#     with open(FILEPATH, 'r') as f:
#         return json.load(f)
def get_json_data():
    if os.path.getsize(FILEPATH) == 0:
        return []  # file is empty, return empty list
    with open(FILEPATH, 'r') as f:
        return json.load(f)

def save_json_data(data):
    with open(FILEPATH, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 2:
        print("Please provide a command.")
        sys.exit(1)
    
    command = argv[1]

    if command == "add":
        data = get_json_data()
        task_id = len(data) + 1
        task = Task(task_id, argv[2], "todo")
        data.append(task.__dict__)
        save_json_data(data)
        print(f"Task {task_id} added.")
        
    elif command == "update":
        if len(argv) < 4:
            print("Usage: update <id> <new_description>")
            sys.exit(1)
        data = get_json_data()
        task_id = int(argv[2])
        updated = False
        for task in data:
            if task['id'] == task_id:
                task['description'] = argv[3]
                updated = True
                break
        if updated:
            save_json_data(data)
            print(f"Task {task_id} updated.")
        else:
            print(f"Task {task_id} not found.")
            
    elif command == "delete":
        data = get_json_data()
        task_id = int(argv[2])
        deleted = False

        for task in data:
            if task['id'] == task_id:
                data.remove(task)
                deleted = True
                break  # task found and removed, exit loop

        if deleted:
            save_json_data(data)
            print(f"Task {task_id} deleted.")
        else:
            print(f"Task {task_id} not found.")
            
    elif command == "mark-in-progress":
        data = get_json_data()
        task_id = int(argv[2])
        
        marked = False
        
        for task in data:
            if task['id'] == task_id:
                task['status'] = "in-progress"
                marked = True
                break
            
        if marked:
            save_json_data(data)
            print(f"Task {task_id} status changed to in-progress.")
        else:
            print(f"Task {task_id} not found.")
            
    elif command == "mark-done":
        data = get_json_data()
        task_id = int(argv[2])
        
        marked = False
        
        for task in data:
            if task['id'] == task_id:
                task['status'] = "done"
                marked = True
                break
            
        if marked:
            save_json_data(data)
            print(f"Task {task_id} status changed to done.")
        else:
            print(f"Task {task_id} not found.")
    
    elif command == "list":
        data = get_json_data()
        pp = pprint.PrettyPrinter(indent=4)
        # pprint.pp(data)
        for task in data:
            pprint.pp(task)
            
    elif command == "list-todo":
        data = get_json_data()
        pp = pprint.PrettyPrinter(indent=4)
        for task in data:
            if task['status'] == "todo":
                pprint.pp(task)
                
    elif command == "list-in-progress":
        data = get_json_data()
        pp = pprint.PrettyPrinter(indent=4)
        for task in data:
            if task['status'] == "in-progress":
                pprint.pp(task)
                
    elif command == "list-done":
        data = get_json_data()
        pp = pprint.PrettyPrinter(indent=4)
        for task in data:
            if task['status'] == "done":
                pprint.pp(task)