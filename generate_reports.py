from pathlib import Path
from task_list import t_list
from datetime import datetime
from read_user import read_username


#create the report file if the do not exist.
def generate_files():
    #Create task_overview.txt and user_overview.txt if they don't exist.
    Path("task_overview.txt").touch(exist_ok=True)
    Path("user_overview.txt").touch(exist_ok=True)

#pull together task info
def task_info():
    today = datetime.today() #todays date to use when checking if task is overdue
    tasks = t_list()

    #variables to store task info
    num_of_tasks = len(tasks)
    uncompleted_tasks = 0
    overdue_tasks = 0
    
    #iterate through the task list and gather the task info
    for task in tasks:
        if task['completed'] == "Yes":
            continue
        uncompleted_tasks += 1
        if task['due_date'] < today:
            overdue_tasks += 1 

    #Variables to store info and calculate percentages
    completed_tasks = len(tasks) - uncompleted_tasks
    percentage_imcomplete = round((uncompleted_tasks / num_of_tasks) * 100)
    percentage_overdue = round((overdue_tasks / num_of_tasks) * 100)

    return num_of_tasks, completed_tasks, uncompleted_tasks, overdue_tasks, percentage_imcomplete, percentage_overdue

#Format to write the task info to the task_overview.txt file    
def write_task_overview(num_of_tasks, completed_tasks, uncompleted_tasks,overdue_tasks, percentage_imcomplete, percentage_overdue):
    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(f'''Task Info:\nTotal number of Tasks: {num_of_tasks}
Number of completed tasks: {completed_tasks}
Number of uncompleted tasks: {uncompleted_tasks}
Number of overdue tasks: {overdue_tasks}
Percentage of imcomplete tasks: {percentage_imcomplete}%
Percentage of overdue tasks: {percentage_overdue}%''')

#Generates the reports and reads them to the terminal
def generate_task_report():
    generate_files()
    num_of_tasks, completed_tasks, uncompleted_tasks, overdue_tasks, percentage_imcomplete, percentage_overdue = task_info()
    write_task_overview(num_of_tasks, completed_tasks, uncompleted_tasks, overdue_tasks, percentage_imcomplete, percentage_overdue)
    
    try:
        with open("task_overview.txt", "r") as task_overview:
            print(task_overview.read())
    except FileNotFoundError:
        print("Error file does not exist!")

#calculate the user info, writes to the user_overview txt doc and print to console.     
def generate_user_report():
    users = read_username()
    tasks = t_list()
    today = datetime.today()

    user_tasks = {user: {'total': 0, 'completed': 0, 'incompleted': 0, 'overdue': 0} for user in users} #store the info for users tasks

    for task in tasks:
        user = task['username']
        user_tasks[user]['total'] += 1

        if task['completed'] == 'Yes':
            user_tasks[user]['completed'] += 1
        elif task['completed'] == 'No' and task['due_date'] < today: #check due date against todays date
            user_tasks[user]['overdue'] += 1
        elif task['completed'] == 'No':
            user_tasks[user]['incompleted'] += 1

    try: #check if txt file exists 
        with open("user_overview.txt", "w") as user_overview:
            user_overview.write(f"\nUser Info:\nTotal number of users: {len(users)}\nTotal number of tracked tasks: {len(tasks)}\n")
            for user in users:
                p_of_tasks = round((user_tasks[user]['total'] / len(tasks)) * 100)
                #try, except block to catch 0 division errors
                try:
                    p_of_complete_tasks = round((user_tasks[user]['completed'] / user_tasks[user]['total']) * 100)
                    p_of_incomplete_tasks = round((user_tasks[user]['incompleted'] / user_tasks[user]['total']) * 100)
                    p_of_overdue_tasks = round((user_tasks[user]['overdue'] / user_tasks[user]['total']) * 100)
                except ZeroDivisionError:
                    #allow 0% of tasks, rather than throwing an error.
                    p_of_complete_tasks = 0
                    p_of_incomplete_tasks = 0
                    p_of_overdue_tasks = 0
                #formatt for how tasks are written to file and printed to console. 
                user_overview.write(f"{user} has {user_tasks[user]['total']} tasks\n"
                                    f"\t\t  {p_of_tasks}% of all tasks\n"
                                    f"\t\t  {p_of_complete_tasks}% completed tasks\n"
                                    f"\t\t  {p_of_incomplete_tasks}% incomplete tasks\n"
                                    f"\t\t  {p_of_overdue_tasks}% overdue tasks.\n")

        with open("user_overview.txt", "r") as user_overview:
            print(user_overview.read())
    except FileNotFoundError:
        print("Error file does not exist.")
    


