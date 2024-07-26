password = input("Enter the password: ")

def lengthCheck(password):
    if len(password)<6 or len(password)>20:
        return False
    return True

def character_check(password):
    containLowerCase = False
    containUpperCase = False
    for i in password:
        if 97 <= ord(i) <= 122:
            containLowerCase = True
        if 65 <= ord(i) <= 90:
            containUpperCase = True
    if not containLowerCase or not containUpperCase:
        return False
    return True

def do_not_contain_3row(password):
     for i in range(len(password)-2):
        curr_window = password[i:i+3]
        if curr_window.count(curr_window[0]) == len(curr_window):
            flag = False
     return flag

def isStrong(password):
    flag = True

    # password length check
    flag = lengthCheck(password)

    # charcter check
    flag = character_check(password)

    # do not contain 3 character in a row check 
    flag = do_not_contain_3row(password)

    return flag

if isStrong(password):
    print(0)
else:
    if not lengthCheck(password):
        current_length = len(password)
        if current_length < 6:
            remaining_character_needed = 6 - current_length
            

    




    
    
        

    


