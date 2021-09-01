import linecache
import random
import os
import sys
import hashlib

from randompassword import rand_password
from masterpassword import master_password

master_password()

while True:
    input_var = input('What do you want: ')

    file = open('storage/passwordstore.txt','r')
    password_store = file.read()
    file.close()

    #Creates a new password
    if input_var == 'new password':
        new_name = input('Name: ')
        new_password = input('Password: ')
        if new_password == 'random':
            new_password = rand_password()
        file = open('storage/passwordstore.txt', 'a')
        file.write('\nNAME: ' + str(new_name) + ' --- PASSWORD: ' + str(new_password) + '\n')
        file.close()

    #Clears all previous passwords
    elif input_var == 'clear':
        pwd_clear = input('Are you sure you want to do this, it cannot be undone: Y or N: ')
        mp_clear = input('Do you want to clear the master password as well? Y or N: ')

        if pwd_clear == 'Y' or pwd_clear == 'y':
            file = open('storage/passwordstore.txt', 'w')
            file.write('')
            file.close()
            pwd_clear = True

        if mp_clear == 'Y' or mp_clear == 'y':
            file = open('storage/masterpassword.txt', 'w')
            file.write('')
            file.close()
            mp_clear == False

        if pwd_clear and mp_clear:
            print('Passwords and Master password cleared.')
        elif pwd_clear:
            print('Passwords cleared.')
        elif mp_cleared:
            print('Master password cleared.')



    #Quits program
    elif input_var == 'quit':
        quit()

    #Prints all passwords
    elif input_var == 'print all':
        if password_store != '':
            file = open('storage/passwordstore.txt', 'r')
            print(file.read())
            file.close()
        else:
            print('You have no saved passwords.')

    #Generates a random password
    elif input_var == 'random password':
        print(rand_password())

    elif input_var == 'hello_world':
        print('I work')

    #Searches for specified password
    with open('storage/passwordstore.txt', 'r') as search_file:
        for line in search_file:
            if input_var in line:
                print('')
                print(line)
