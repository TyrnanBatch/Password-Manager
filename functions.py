
# if input_var == 'new password':
#     new_name = input('Name: ')
#     new_password = input('Password: ')
#     if new_password == 'random':
#         new_password = rand_password()
#     file = open('storage/passwordstore.txt', 'a')
#     file.write('\nNAME: ' + str(new_name) +
#                ' --- PASSWORD: ' + str(new_password) + '\n')
#     file.close()

#  # Clears all previous passwords
# elif input_var == 'clear':
#     pwd_clear = input(
#         'Are you sure you want to do this, it cannot be undone: Y or N: ')
#     mp_clear = input(
#         'Do you want to clear the master password as well? Y or N: ')

#     if pwd_clear == 'Y' or pwd_clear == 'y':
#         file = open('storage/passwordstore.txt', 'w')
#         file.write('')
#         file.close()
#         pwd_clear = True

#     if mp_clear == 'Y' or mp_clear == 'y':
#         file = open('storage/masterpassword.txt', 'w')
#         file.write('')
#         file.close()
#         mp_clear == False

#     if pwd_clear and mp_clear:
#         print('Passwords and Master password cleared.')
#     elif pwd_clear:
#         print('Passwords cleared.')
#     elif mp_clear:
#         print('Master password cleared.')

#     # Quits program
def quit_func():
    quit()

def rand_password():
    import random
    import linecache

    rand_adj = random.randint(2 , 229)
    rand_noun = random.randint(233 , 604)
    rand_verb = random.randint(607 , 2110)
    rand_adverb = random.randint(2113 , 2442)

    adjective = linecache.getline('storage/source.txt',rand_adj)
    noun = linecache.getline('storage/source.txt',rand_noun)
    verb = linecache.getline('storage/source.txt',rand_verb)
    adverb = linecache.getline('storage/source.txt',rand_adverb)

    password = str(adjective) + str(noun) + str(verb) + str(adverb)
    password = str.join(' ', password.splitlines())
    password = password.replace(' ', '')
    password = password.lower()

    return password
#     # Prints all passwords
# elif input_var == 'print all':
#     if password_store != '':
#         file = open('storage/passwordstore.txt', 'r')
#         print(file.read())
#         file.close()
#     else:
#         print('You have no saved passwords.')

# # Generates a random password
# elif input_var == 'random password':
#     print(rand_password())

# elif input_var == 'hello_world':
#     print('I work')

#     # Searches for specified password
# with open('storage/passwordstore.txt', 'r') as search_file:
#     for line in search_file:
#         if input_var in line:
#             print('')
#             print(line)
