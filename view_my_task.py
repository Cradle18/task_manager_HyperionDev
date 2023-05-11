from logged_in import get_curr_user
from task_list import t_list
from datetime import datetime, date


DATETIME_STRING_FORMAT = "%Y-%m-%d"

def display_task(task):
    #Format and display a single task.
    disp_str = f"Task reference:\t {task['task_reference']}\n"
    disp_str += f"Task: \t\t {task['title']}\n"
    disp_str += f"Assigned to: \t {task['username']}\n"
    disp_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Task completed? \t{task['completed']}\n" 
    disp_str += f"Task Description: \n{task['description']}\n"
    
    print(disp_str)


def view_my_tasks():
    #Retrieve and display all tasks assigned to the current user.
    while True:
        tasks = t_list()
        for task in tasks:
            if task['username'] == get_curr_user() and task['completed'] !='Yes': #if a task is marked as complete it will not show.
                display_task(task)
        #Asks the user if they would like to edit or complete one of the tasks.
        reference_number = input("Enter the reference number of the task you want to edit or -1 to return to the menu: ")
        if reference_number == "-1":
            break
        try:
            action = input("Enter 'u' to update the username, 'd' to update the duedate or 'c' to mark the task as complete: ")
            if action == "u":
                new_username = input("Enter the new username: ")
                edit_task(reference_number, new_username=new_username)
            elif action == "c":
                completed = input("Enter 'Yes' to mark the task as complete or 'No' to mark it as incomplete: ")
                edit_task(reference_number, completed=completed)
            elif action == "d":
                due_date = input("Enter new due date (yyyy-mm-dd): ")
                edit_task(reference_number, due_date=due_date)
            else:
                print("Invalid action.")
        except ValueError:
            print("Invalid input!")

#updates the task with the edits.
def edit_task(reference_number, new_username=None, completed=None, due_date=None):
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    found = False
    for i, task in enumerate(tasks):
        if task.startswith(reference_number):
            fields = task.strip().split(";")
            if new_username is not None:
                fields[1] = new_username
            if completed is not None:
                fields[6] = completed
            if due_date is not None:
                fields[4] = due_date
            tasks[i] = ";".join(fields) + "\n"
            found = True
            break
    if found:
        with open("tasks.txt", "w") as f:
            f.writelines(tasks)
        print("Task updated successfully!")
    else:
        print("Task not found.")
          
