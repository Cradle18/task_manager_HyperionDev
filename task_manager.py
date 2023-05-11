"""
This is a task manager programme, that allows users to create others users, create user tasks and edit user tasks.
Admin can then view all task information, other users can see and edit there own tasks and also view all tasks.
"""

# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password

#=====importing libraries===========
from logged_in import log_in
from view_menu import view_menu

log_in()

view_menu()