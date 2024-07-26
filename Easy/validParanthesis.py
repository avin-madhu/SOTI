paranthesis = input("Enter the paranthesis string: ")

def longestValidParanthesis(paranthesis):
    stack = []
    count = 0
    for i in paranthesis:
        if stack and i == ")" and stack[-1] == "(":
                stack.pop()
                count += 2
        else:
            stack.append(i)
    return count 

print(longestValidParanthesis(paranthesis))
            