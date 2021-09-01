import tkinter as tk

root = tk.Tk()
root.configure(bg = 'grey')
root.title('Password Manager')

from masterpassword import master_password_func

show_text = '*'

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
    request_text = 'Enter new Master Password: '
except:
    request_text = 'Enter Master Password: '

request = tk.Label(root, font = 'Times 20 bold italic', width = 62, text = request_text)
request.grid(row = 1, column = 0, columnspan = 2)

master_password_input = tk.Entry(root, justify = 'center', width = 30, font = 'Times 40 bold italic', bd = 5, show = show_text)
master_password_input.grid(row = 2, column = 0)

show_button = tk.Button(root, height = 2, width = 12, bd = 10, text = 'show', font = 'Times 16 bold italic', command = show_button)
show_button.grid(row = 2, column = 1)

master_password_submit = tk.Button(root, height = 2, width = 42, bd = 10, text = 'Submit', font = 'Times 30 bold italic', command = master_password_read)
master_password_submit.grid(row = 3, column = 0, columnspan = 2)

root.mainloop()
