from read_user import read_username
from pathlib import Path

current_user = None 

def gen_user_text():
    #create file path
    user_file_path = Path("user.txt")
    #check if file already exists, if not, write user.txt with admin;password
    try:
        if user_file_path.is_file():
            pass
        else:
            with open(user_file_path, "w") as user_file:
                user_file.write("admin;password" + "\n")
    except Exception as e:
        print("An error occured {e}")


#Authenticates the users credentials and returns a boolean value and also returns the username upon success.
def authenticate_user(username, password, username_password): 
    if username not in username_password.keys():
        print("User does not exist!")
        return False 
    elif username_password[username] != password:
        print("Wrong password!")
        return False
    else:
        print("Login Succesful!")
        return username

#Gets the user inputs for username and password and returns a tuple.
def get_user_credentials(): 
    print("Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

#calls get_user_credentials to get user inputs and then passes them into authenticate_user to check credentials are valid.
def log_in():
    gen_user_text()
    username_password = read_username()
    while True:
        username, password = get_user_credentials()
        current_username = authenticate_user(username, password, username_password)
        #checks current username to get the current user.
        if current_username:
            global current_user
            current_user = current_username
            return True

#store the current user logged in.
def get_curr_user():
    username = current_user
    return username




