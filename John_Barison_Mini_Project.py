# To-Do List apllication
# Essential variables
tasks = []
completed_tasks = []

# Code lines 7 and 8 are to get the user's name and and what they would like to do.
user_name = input("Please enter your name? ")
print(f"Hello {user_name}, what would you like to do today😊")

# Code lines 11 to 16 is a function to add a new task to the to-do list.
def add_task():    
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        if len(tasks) == 1:
            print(f"Congratulations {user_name} on adding your very first task!🥳 and taken a step towards productivity and a solid routine🔥 You've got this💪")
        print(f"Task '{new_task}' added successfully.\n\n")

# Code lines 19 to 25 is a function to view all pending tasks.
def view_tasks():
        if len(tasks) == 0:
            print("You currently have no pending tasks.")
        else:
            print("All Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}\n\n")

# Code lines 28 to 39 is a function to mark a task as completed and move it to a completed tasks list.
def mark_task():
    if len(tasks) == 0:
        print("There are no tasks to consider.\n\n")
    else:
        view_tasks()
        task_num = int(input("Select the completed task: "))
        if 1 <= task_num <= len(tasks):
            completed_task = tasks.pop(int(task_num) - 1)
            completed_tasks.append(completed_task)
            print(f"Task '{completed_task}' marked as completed.\n\n")
        else:
            print("Invalid task number.\n\n")

# Code lines 42 to 52 is a function to delete a task from the to-do list.            
def delete_task():
    if len(tasks) == 0:
        print("There are no tasks to delete.\n\n")
    else:
        view_tasks()
        task_num = int(input("Select the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(int(task_num) - 1)
            print(f"Task '{deleted_task}' deleted successfully.\n\n")
        else:
            print("Invalid task number.\n\n")
        
# Code lines 55 to 74 is a loop to keep the application running until the user decides to exit.
while True:
    # Code lines 57 to 62 are to display the menu, get the user's choice and then check if the user's choices are valid.
    print("1. Add a new task\n2. View existing tasks\n3. Mark task as completed\n4. Delete a task\n5. Exit")
    user_choice = int(input("Proceed by entering your choice (1-5): "))
    # if type(user_choice) != int: 
    #     print("Invalid input, please enter a number between 1 and 5.\n\n")
    if user_choice < 1 or user_choice > 5:
        print("Invalid choice, please select a number between 1 and 5.\n\n")
    # Code lines 64 to 74 are to call the appropriate function based on the user's choice.
    if user_choice == 1:
        add_task()
    elif user_choice == 2:
        view_tasks()
    elif user_choice == 3:
        mark_task()
    elif user_choice == 4:
        delete_task()
    elif user_choice == 5:
        print(f"Remember {user_name}, you've got this💪. Have a productive day ahead!👋")
        break