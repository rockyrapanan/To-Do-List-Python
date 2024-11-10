import time
import datetime  # Importing datetime module

# Name: Leonardo L. Rapanan
# Project: To Do List

# Using empty arrays to store user information.
user_name = []         # Username store array
user_email = []        # User email store array
password = []          # Password store array
date_time = []         # Date and time store array
task = []              # Task store array
complete_task = []     # Complete task store array
past_task = []         # Past task store array (this was missing)

# Program introduction.
print("Hello, this is Ethan to-do")
time.sleep(2)
print("I am your personal to-do list application")
time.sleep(2)
print("First, we are going to input your information")
time.sleep(2)
print("Such as a username, email, and password")
time.sleep(2)
print("Now let's input your information")
time.sleep(2)

# Collect user name and store in user_name array.
user = input("Enter a username: ")
user_name.append(user)
# Collect user email and store in user_email array
email = input("Enter your email: ")
user_email.append(email)
# Program prints user's username and email.
print("Your username:", *user_name)
print("Your email:", *user_email)
time.sleep(2)

# Collect user password and store in password array.
user_pass = input("Enter a password: ")
password.append(user_pass)

# Login validation loop.
while True:
    # User inputs username and password.
    login = input("Enter username: ")
    pass_w = input("Enter password: ")

    # Validate credentials by checking the first items in the lists
    if login == user_name[0] and pass_w == password[0]:
        print("Login Successful")
        
        # To-do program loop.
        while True:
            # main program start.
            time.sleep(2)
            # Program prins out list.
            print("Here are Task list options:")
            time.sleep(2)
            print("1: Add task")
            print("2: View your tasks")
            print("3: Complete tasks")
            print("4: Exit To-do app.")
            # user inputs from option from list 1 - 4.
            choose = int(input("Choose your option: "))
            # If user chooses 1
            if choose == 1:
                # User enters task
                user_task_input = input("Enter your task: ")
                # Corrected datetime usage
                current_date_time = datetime.datetime.now()  
                # date and time stored in date_time
                date_time.append(current_date_time)
                task.append(user_task_input)
                print("Your task has been entered!")
            # If user chooses 2
            elif choose == 2:
                # View tasks with corresponding date/time
                if task:
                    print("You entered these tasks:")
                    for idx, task_item in enumerate(task, start=1):
                        # Get the date and time for each task.
                        # Task has index start as 1
                        task_time = date_time[idx - 1]
                        # program prints index number with task and date with time task was created.
                        print(f"{idx}. {task_item} - Date and Time: {task_time.strftime('%A, %B %d, %Y %I:%M %p')}")
                else:
                    # Tells user no task are stored in task array.
                    print("Your To-Do list is empty")
            # if user chooses 3        
            elif choose == 3:
                # "if" statement. Program tells user to choose a task to complete.
                if task:
                    print("Choose a task to complete:")
                    # for loop idx is printing array number start as 1 and print task item.
                    for idx, task_item in enumerate(task, start=1):
                        print(f"{idx}. {task_item}")
                    # program ask user which task they want to mark as complete.
                    task_to_complete = int(input("Enter the task number you want to complete: "))
                    # When user inputs a task they want completed.
                    if 1 <= task_to_complete <= len(task):
                        completed_task = task.pop(task_to_complete - 1)  # Remove from task and add to completed_task
                        completed_time = date_time.pop(task_to_complete - 1)
                        complete_task.append(completed_task)  # Add to completed tasks list
                        past_task.append((completed_task, completed_time))  # Optionally, keep a history of completed tasks
                        # Program prints the task completed along with a date and time when it was completed.
                        print(f"Task '{completed_task}'  marked as completed at {completed_time.strftime('%A, %B %d, %Y %I:%M %p')}")
                    else:
                        # When user inputs an  invalid task number
                        print("Invalid task number!")
                else: # When enters option 4 with no task.
                    print("Your To-Do list is empty, no tasks to complete.")
                    break
            # If user wants to exit the ptogram.      
            elif choose == 4:
                print("Exiting the to-do list program.")
                break  # Exit the task loop and the program
            else: # Program lets user know that their are only 4 options 1 - 4.
                print("Invalid choice, please select 1, 2, 3, or 4.")
        break
    else: # Whe user gets username or password wrong.
        print("Invalid username or password. Please try again!")