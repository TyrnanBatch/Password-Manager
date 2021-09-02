def master_password_entry():
    import tkinter as tk
    import time

    from masterpassword import master_password_func

    root = tk.Tk()
    root.configure(bg = 'grey')
    root.title('Password Manager')

    def master_password_read():
        result = master_password_input.get()
        if master_password_func(result):
            root.destroy()
            return True
        else:
            print('INCORRECT')


    try:
        file = open("storage/masterpassword.txt","r")
        master_password = file.read()
        file.close()
        request_text = 'Enter new Master Password: '
    except:
        request_text = 'Enter Master Password: '

    request = tk.Label(root, font = 'Times 20 bold italic', width = 21, height = 2, text = request_text)
    request.grid(row = 1, column = 1,)

    master_password_input = tk.Entry(root, justify = 'center', width = 25, font = 'Times 40 bold italic', bd = 5, show = '*')
    master_password_input.grid(row = 1, column = 2)

    master_password_submit = tk.Button(root, height = 1, width = 44, bd = 10, text = 'SUBMIT', font = 'Times 30 bold italic', command = master_password_read)
    master_password_submit.grid(row = 2, column = 1, columnspan = 2)

    master_password_reset = tk.Button(root, height = 6, text = 'Reset Master Password', font = 'Times 15 bold italic', bd = 10)
    master_password_reset.grid(row = 1, column = 3, rowspan = 2)

    root.mainloop()

def password_manager_gui():

    import tkinter as tk

    from functions import quit_func

    root = tk.Tk()

    quit_button = tk.Button(root, command = quit_func).grid(row = 1, column = 1)
