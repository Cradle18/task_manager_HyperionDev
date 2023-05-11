from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

#reads the tasks txt file and returns the data into a list.
def read_tasks():
    with open("tasks.txt", "r") as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]
    return task_data

#changes the task_data into a dict.
def create_task_dict(task_str):
        task_components = task_str.split(";")
        return {
            'task_reference': task_components[0],
            'username': task_components[1],
            'title': task_components[2],
            'description': task_components[3],
            'due_date': datetime.strptime(task_components[4], DATETIME_STRING_FORMAT),
            'assigned_date': datetime.strptime(task_components[5], DATETIME_STRING_FORMAT),
            'completed': 'Yes' if task_components[-1] == 'Yes' else 'No' 
        }
    
def create_task_list(task_data):
    task_list = [create_task_dict(task_str) for task_str in task_data]
    return task_list

def t_list():
    task_data = read_tasks()
    task_list = create_task_list(task_data)
    return task_list


