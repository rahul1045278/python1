class Task:
  def __init__(self, description):
    self.description = description
    self.completed = False

  def mark_completed(self):
    self.completed = True

  def __str__(self):
    status = "Completed" if self.completed else "Pending"
    return f"- [{status}] {self.description}"

# Define functions for managing tasks
tasks = []

def add_task(description):
  tasks.append(Task(description))
  print(f"Task '{description}' added to the list!")

def view_tasks():
  if not tasks:
    print("There are no tasks in the list.")
    return
  print("Your To-Do List:")
  for task in tasks:
    print(task)

def mark_task_complete(index):
  if index < 0 or index >= len(tasks):
    print("Invalid task index.")
    return
  tasks[index].mark_completed()
  print(f"Task '{tasks[index].description}' marked as completed.")

def delete_task(index):
  if index < 0 or index >= len(tasks):
    print("Invalid task index.")
    return
  del tasks[index]
  print(f"Task deleted from the list.")

# Main loop for user interaction
while True:
  print("\nTo-Do List App")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Complete")
  print("4. Delete Task")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    description = input("Enter task description: ")
    add_task(description)
  elif choice == '2':
    view_tasks()
  elif choice == '3':
    view_tasks()
    index = int(input("Enter the index of the task to mark complete: ")) - 1
    mark_task_complete(index)
  elif choice == '4':
    view_tasks()
    index = int(input("Enter the index of the task to delete: ")) - 1
    delete_task(index)
  elif choice == '5':
    print("Exiting To-Do List App.")
    break
  else:
    print("Invalid choice. Please try again.")
