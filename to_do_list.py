import time
import datetime  # Importing datetime module

# Dictionary to store user credentials
user_data = {}

# Arrays to store task information
date_time = []         # Date and time storage array
task = []              # Task storage array
complete_task = []     # Completed tasks array
past_task = []         # Past tasks array
# function to create user account
def create_account(username, password):
    """Creates an account if the username is unique."""
    if username in user_data:
        print("Username already exists. Try a different username.")
    else: 
        user_data[username] = password
        print("Account created successfully!")
# function to login user account
def login_user(username, password):
    """Logs in the user if credentials match."""
    if username in user_data and user_data[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Try again.")
        return False

def add_task(task_description):
    """Adds a task with the current timestamp."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_time.append(current_time)
    task.append(task_description)
    print(f"Task '{task_description}' added on {current_time}")

def view_tasks():
    """Displays all tasks."""
    print("\nYour To-Do List:")
    if not task:
        print("No tasks to display.")
    else:
        for i, t in enumerate(task, start=1):
            print(f"{i}. {t} - Added on {date_time[i-1]}")
    print("\n")

def complete_task(task_number):
    """Marks a task as completed and moves it to the completed list."""
    if 0 < task_number <= len(task):
        completed = task.pop(task_number - 1)
        date_completed = date_time.pop(task_number - 1)
        complete_task.append(completed)
        past_task.append(date_completed)
        print(f"Task '{completed}' marked as completed.")
    else:
        print("Invalid task number.")

# Greeting and registration
print("Hello, my name is Ethan To-Do!")
time.sleep(2)
print("I'm your personal To-Do list application.")
time.sleep(2)
print("I can add, complete, and let you view your to-do list items.")
time.sleep(2)
print("Let's get you registered.")
time.sleep(2)

# Account setup
user_input = input("Input username: ")
user_pass = input("Input password: ")
create_account(user_input, user_pass)

# Login prompt
print("\nPlease log in to continue.")
username = input("Username: ")
password = input("Password: ")

if login_user(username, password):
    # Main loop for to-do list management
    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Complete a task")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            task_description = input("Enter the task: ")
            add_task(task_description)
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            view_tasks()  # Show tasks first for reference
            try:
                task_number = int(input("Enter the task number to complete: "))
                complete_task(task_number)
            except ValueError:
                print("Please enter a valid task number (integer).")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Login failed. Exiting program.")
