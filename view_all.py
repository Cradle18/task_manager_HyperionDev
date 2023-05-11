from task_list import t_list
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def view_all():
    task_list = t_list()
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n{t['description']}"
        print(disp_str + "\n")

