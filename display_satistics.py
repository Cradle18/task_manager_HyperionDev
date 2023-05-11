from pathlib import Path
from task_list import t_list
from read_user import read_username

#check if user.txt and tasks.txt exist before displaying satistics.
def check_text_files():
    #define file paths.
    users_file = Path("user.txt")
    tasks_file = Path("tasks.txt")
    
    #check if file exist.
    try:
        if users_file.is_file:
            pass
        else:
            with open(users_file,"w") as user_text_file:
                user_text_file.write("admin;password" + "\n")
        if tasks_file.is_file:
            pass
        else:
            tasks_file.touch(exist_ok=True) 
    except Exception as e:
        print("A error occured: {e}")

#display num of users and task to the terminal after files exist check has been complete
def display_satistics():
    #call txt files check
    check_text_files()

    #declare variable for the read files
    users = read_username()
    tasks = t_list()

    #take the length of each variable, as this is the total number
    total_tasks = len(tasks)
    total_users = len(users)
    
    #print to terminal
    print("-----------------------------------")
    print(f"Total Number of users: \t\t {total_users}")
    print(f"Total Number of tasks: \t\t {total_tasks}")
    print("-----------------------------------")



