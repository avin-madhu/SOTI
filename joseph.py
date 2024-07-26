# 10

def convertToBinary(num):
    binary_result = ""
    while num:
        rem = num%2
        binary_result += str(rem)
        num //= 2
    return int(binary_result[::-1])

def toggleDigits(bin_num):
    bin_string = str(bin_num)
    toggled_string = ""
    for i in bin_string:
        if i == '1':
            toggled_string += '0'
        else:
            toggled_string += '1'
    return toggled_string

def converToDecimal(bin_num):
    exp = 0
    res = 0
    for i in range(len(bin_num)-1, -1, -1):
        if bin_num[i] == '1':
            res += 2**exp
            exp+=1
        else:
            exp+=1
            continue
    return res

bin_num = convertToBinary(10)
toggled = toggleDigits(bin_num)
print(converToDecimal(toggled))





