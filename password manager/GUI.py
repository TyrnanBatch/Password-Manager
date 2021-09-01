import tkinter as tk
root = tk.Tk()
root.configure(bg = 'grey')

from masterpassword import master_password_func

show_text = ''

def master_password_read():
    result = master_password_input.get()
    if master_password_func(result):
        print('Success')
    else:
        print('Fail')

def show_button():
    global show_text
    if show_text == '*':
        show_text = ''
    elif show_text ==  '':
        show_text = '*'
    print(show_text)

try:
    file = open("storage/masterpassword.txt","r")
    master_password = file.read()
    file.close()
    entry_text = 'Enter new Master Password: '
except:
    entry_text = 'Enter Master Password: '

root.title(entry_text)

master_password_input = tk.Entry(root, justify = 'center', width = 29, highlightcolor = 'red', bd = 5, show = show_text).grid(row = 1, column = 0)

show_button = tk.Button(
root, height = 1, width = 6, bd = 5, text = 'show', font = 'Times 8 bold italic', command = show_button).grid(row = 1, column = 1)

master_password_submit = tk.Button(
root, height = 1, width = 20, bd = 5, text = 'Submit', font = 'Times 15 bold italic', command = master_password_read).grid(row = 2, column = 0, columnspan = 2)

root.mainloop()
