string = input("Enter the string: ")

def isPalindrome(string):
    i,j = 0, len(string)-1
    while i < j :
        if string[i] != string[j]:
            return False
        i+=1
        j-=1
    return True

if isPalindrome(string):
    print("Palindrome")
else:
    print("not a palindrome")
    
