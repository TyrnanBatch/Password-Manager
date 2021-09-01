def master_password_func(input):

    import hashlib

    master_password = 'place_holder'
    file_check = False

    try:
        file = open("storage/masterpassword.txt","r")
        master_password = file.read()
        file.close()
    except:
        file_check = True

    if master_password == '' or file_check:
        input = hashlib.md5(input.encode()).hexdigest()
        file = open("storage/masterpassword.txt","w")
        file.write(input)
        file.close()
        return True
    else:
        input = hashlib.md5(input.encode()).hexdigest()
        if str(input) == str(master_password):
            return True
