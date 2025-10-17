squares = [(x+1)**2 for x in range(10)]
print(squares)
squares = [(x)**2 for x in range(10)]
print(squares)
even = [x for x in range(100) if x%2 ==0]
print(even)
odd = [x for x in range(100) if x%2 !=0]
print(odd)
'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
'''


numbers = [1,2,3,4,5,6]
squares = map(lambda x: x**2 ,numbers)
print(list(squares))
odd = filter(lambda x: x%2 !=0,numbers)
print(list(odd))
from functools import reduce
product = reduce(lambda x , y : x*y ,numbers)
print(product)
'''
[1, 4, 9, 16, 25, 36]
[1, 3, 5]
720
'''


import os

# File to store tasks
FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip(). split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")
            
# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added.")
    
# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")

# Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task ID not found.")
        

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to Delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Task ID not found.")
        
# Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye")
            break
        else:
            print("Invalid Choice. Please try again")
            
if __name__ == "__main__":
    main()
    
'''
Task Manager Menu:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
Enter your choice: 1
Enter task title: kmkmck
Task 'kmkmck' added.

Task Manager Menu:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
Enter your choice: 2
[1] kmkmck - incomplete

Task Manager Menu:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
Enter your choice: 3
Enter task ID to mark as complete: 1
Task 'kmkmck' marked as complete.

Task Manager Menu:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
Enter your choice: 2
[1] kmkmck - complete

Task Manager Menu:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
Enter your choice: 4
Enter task ID to Delete: 1
Task 'kmkmck' deleted.

Task Manager Menu:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
Enter your choice: 2
No tasks available.

Task Manager Menu:
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
Enter your choice: 5
Goodbye
'''