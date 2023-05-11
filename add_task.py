from datetime import datetime, date
from read_user import read_username
from pathlib import Path

DATETIME_STRING_FORMAT = "%Y-%m-%d"

#generate task.txt if does not exist.
def gen_task_file():
    Path("tasks.txt").touch(exist_ok=True)

#This function creates the task into a dict while checking for errors.
def create_task():
    username_password = read_username() #gets a dict of users  

    while True: #Username check, to add user name against task.
        task_username = input("Name of person assigned to task: ")
        if task_username in username_password.keys():
            task_ref = input("Enter task reference (staring with first letter of username, then 0 e.g T0): ")
            task_title = input("Title of task: ")
            task_description = input("Description of task: ")
            break
        else:
            print("User does not exist. Please enter a valid user.")
    
    while True: #Checks valid date format.
        try:
            task_due_date = input("Due date of task? (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Pleae use the format specified.")

    curr_date = date.today()
    new_task = {
            "task_reference": task_ref,
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }
    return new_task

#This function writes the task to the txt file, correctly formatted, while checking for errors.   
def write_task_to_file(task):
    try:
        with open("tasks.txt", "a") as task_file:
            str_attrs = [
                task["task_reference"],
                task["username"],
                task["title"],
                task["description"],
                task["due_date"].strftime(DATETIME_STRING_FORMAT),
                task["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                "Yes" if task["completed"] else "No"
            ]
            formatted_task = ";".join(str_attrs)
            task_file.write("\n" + formatted_task)
        print("Task added succesfully!")
    except IOError:
        print("Error writing to task.txt file.")

#Creates the task and adds it to the txt file.
def add_task():
    gen_task_file()
    new_task = create_task()
    write_task_to_file(new_task)


