from reg_user import reg_user
from add_task import add_task
from view_all import view_all
from view_my_task import view_my_tasks
from logged_in import get_curr_user
from generate_reports import generate_task_report, generate_user_report
from display_satistics import display_satistics

#display the menu to the screen and takes in a user input, then provides the function for the input.
def view_menu():
    reports = "\ngr - Generate reports" if get_curr_user() == "admin" else "" #check if current user is admin, then display gr if True
    satistics = "\nds - Display Satistics" if get_curr_user() == "admin" else ""#same check as above, then display ds if true
    while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
        menu = input(
            '''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task '''
+ reports + 
satistics +
'''
e - Exit
: ''').lower()
        if menu == "r":
            reg_user()
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all()
        elif menu == "vm":
            view_my_tasks()
        elif menu == "gr":
            generate_task_report()
            generate_user_report()
        elif menu == "ds":
            display_satistics()
        elif menu == "e":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice! Please try again.")