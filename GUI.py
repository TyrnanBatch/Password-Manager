def master_password_entry():
    import tkinter as tk
    import time

    from masterpassword import master_password_func
    from GUI import password_manager_home

    root = tk.Tk()
    root.configure(bg='grey')
    root.title('Password Manager')

    def master_password_read():
        result = master_password_input.get()
        if master_password_func(result):
            root.destroy()
            password_manager_home()
        else:
            print('INCORRECT')

    try:
        file = open("storage/masterpassword.txt", "r")
        master_password = file.read()
        file.close()
        request_text = 'Enter new Master Password: '
    except:
        request_text = 'Enter Master Password: '

    request = tk.Label(root, font='Times 20 bold italic',
                       width=21, height=2, text=request_text)
    request.grid(row=1, column=1,)

    master_password_input = tk.Entry(
        root, justify='center', width=25, font='Times 40 bold italic', bd=5, show='*')
    master_password_input.grid(row=1, column=2)

    master_password_submit = tk.Button(
        root, height=1, width=44, bd=10, text='SUBMIT', font='Times 30 bold italic', command=master_password_read)
    master_password_submit.grid(row=2, column=1, columnspan=2)

    master_password_reset = tk.Button(
        root, height=6, text='Reset Master Password', font='Times 15 bold italic', bd=10)
    master_password_reset.grid(row=1, column=3, rowspan=2)

    root.mainloop()


def password_manager_home():
    import tkinter as tk
    import json

    root = tk.Tk()

    name_result = 'Name: '
    password_result = 'Password: '

    #### SEARCH FUNCTION BEGGINS ####

    name_change_entry = tk.Entry(root, font='Times 20')
    password_change_entry = tk.Entry(root, font='Times 20')

    def password_search_button():
        password_search = search_box.get()
        count = 0
        json_file = open('storage/passwordstore.json', 'r')
        json_file_read = json.load(json_file)
        for search in json_file_read:
            if search["name"] == password_search:
                name_result_text.set(json_file_read[count]["name"])
                password_result_text.set(json_file_read[count]["password"])
            count += 1

    def name_change():
        name_label_text = name_label.cget('text')
        if name_label_text != '':
            name_result.grid_forget()
            name_change_entry.grid(row=2, column=2)

    def password_change():
        password_label_text = password_label.cget('text')
        if password_label_text != '':
            password_result.grid_forget()
            password_change_entry.grid(row=3, column=2)

    def name_submit():
        password_search = name_result_text
        name_change_text = name_change_entry.get()
        password_change_text = password_change_entry.get()
        name_result_text.set(name_change_text)
        name_change_entry.grid_forget()
        name_result.grid(row=2, column=2)

    def password_submit():
        password_change_text = password_change_entry.get()
        password_result_text.set(password_change_text)
        password_change_entry.grid_forget()
        json_file = open('storage/passwordstore.json', 'r')
        json_file_read = json.load(json_file)
        json_file.close()
        count = 0
        for search in json_file_read:
            if search["name"] == password_change_text[1]["name"]: # Issue here
                json_file_read[1]["password"] = password_change_text
                json_file = open('storage/passwordstore.json', 'w')
                json_file.write(json.dumps(json_file_read))
                json_file.close()
                print('password changed')
            count += 1

        password_result.grid(row=3, column=2)

    #### SEARCH FUNCTION BEGGINS ####

    search_box = tk.Entry(root, font='Times 20')
    search_box.grid(row=1, column=2, columnspan=3)

    search_button = tk.Button(root, height=1, bd=3, text='SEARCH',
                              font='Times 15', width=10, command=password_search_button)
    search_button.grid(row=1, column=5, columnspan=2)

    change_name_button = tk.Button(root, height=1, bd=3, text='CHANGE',
                                   font='Times 10', command=name_change)
    change_name_button.grid(row=2, column=5)

    submit_name_button = tk.Button(root, height=1, bd=3, text='SUBMIT',
                                   font='Times 10', comman=name_submit)
    submit_name_button.grid(row=2, column=6)

    change_password_button = tk.Button(root, heigh=1, bd=3, text='CHANGE',
                                       font='Times 10', command=password_change)
    change_password_button.grid(row=3, column=5)

    submit_password_button = tk.Button(root, heigh=1, bd=3, text='SUBMIT',
                                       font='Times 10', command=password_submit)
    submit_password_button.grid(row=3, column=6)

    search_text = tk.Label(root, text='Search: ', font='Times 20')
    search_text.grid(row=1, column=1)

    name_label = tk.Label(root, text='Name: ', font='Times 20')
    name_label.grid(row=2, column=1)

    password_label = tk.Label(root, text='Password: ', font='Times 20')
    password_label.grid(row=3, column=1)

    name_result_text = tk.StringVar()
    name_result_text.set('')
    name_result = tk.Label(
        root, textvariable=name_result_text, font='Times 20')
    name_result.grid(row=2, column=2)

    password_result_text = tk.StringVar()
    password_result_text.set('')
    password_result = tk.Label(
        root, textvariable=password_result_text, font='Times 20')
    password_result.grid(row=3, column=2)

    #### SEARCH FUNCTION ENDS ####

    #### NEW PASSWORD FUNCTION BEGGINS ####


def password_manager_gui():

    import tkinter as tk

    from functions import quit_func

    root = tk.Tk()

    quit_button = tk.Button(root, command=quit_func).grid(row=1, column=1)
