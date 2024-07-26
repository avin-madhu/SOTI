n = int(input("Enter the number: "))

def rle(number_string):
    stack = ""
    res = ""
    for i in range(0, len(number_string)):
        if stack and stack[-1] != number_string[i]:
            res += str(len(stack)) + stack[-1]
            stack = ""
        stack += number_string[i]
    if stack:
        return res + str(len(stack)) + stack[-1]

res = '1'
for i in range(n-1):
    res = rle(res)
print(res)
        