password = input("Enter the password: ")

def moves_to_make_strong(password):
    missing_type = 3
    if any('a' <= c <= 'z' for c in password):
        missing_type -= 1
    if any('A' <= c <= 'Z' for c in password):
        missing_type -= 1
    if any(c.isdigit() for c in password):
        missing_type -= 1

    if len(password) < 6:
        return max(missing_type, 6 - len(password))
    elif len(password) > 20:
        return len(password) - 20 + missing_type
    else:
        repeat = 0
        for i in range(len(password) - 2):
            if password[i] == password[i + 1] == password[i + 2]:
                repeat += 1
        return max(missing_type, repeat)

print(moves_to_make_strong(password))

        


    




    
    
        

    


