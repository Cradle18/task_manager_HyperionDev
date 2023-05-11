from read_user import read_username

#register a new user
def reg_user():
    users = read_username()

    #checks if user already exists 
    while True:
        try:
            new_username = input("New username: ")
            if new_username not in users:
                break
            else:
                print("User already exsists!")
        except Exception as e:
            print(f"Error {e}")
    
    new_password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    
    #checks if the entered password, match the confirmed password
    while True:
        try:
            if new_password == confirm_password:
                print("New user added.")
                users[new_username] = new_password

                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in users:
                        user_data.append(f"{k};{users[k]}")
                    out_file.write("\n".join(user_data))
                break
            else:
                print("Passwords do not match.")
                confirm_password = input("Confirm password: ")
        except Exception as e:
            print(f"Error: {e}")
    
        
