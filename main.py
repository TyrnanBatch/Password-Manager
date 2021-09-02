from GUI import master_password_entry
from GUI import password_manager_gui

from functions import quit_func

master_password_entry()
while not master_password_entry():
    print(master_password_entry())
    master_password_entry()


print('pass')
