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


# alternate implementation

def compress(s):
    res = []
    i = 0
    while i < len(s):
        count = 1
        j = i
        while j+1 < len(s) and s[j+1] == s[i]:
            j += 1
            count += 1
        i = j
        res.append(str(count))
        res.append(s[i])
        i += 1
    
    return "".join(res)


print(compress("3322251"))
print(compress("11112222"))
print(compress("1"))
