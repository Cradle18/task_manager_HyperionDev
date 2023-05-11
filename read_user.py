#read the user.txt file, to create a dict to use in create task, can also be used in other functions.
def read_username():
    try:
        with open("user.txt", "r") as f:
            username_password = {}
            for line in f:
                line = line.strip()
                user_info = line.split(';')
                username = user_info[0]
                password = user_info[1]
                username_password[username] = password
    except IOError:
        print("Error reading file.")

    return username_password

