ipAddress = input("Enter the IP Address: ")

def backtrack(ip_address,segments):
    if len(ip_address) > (4 - len(segments))*3:
        return
    
    if len(segments) == 4:
        res.append('.'.join(segments))
        return 
    
    for i in range(min(3, len(ip_address))):
        current = ip_address[:i+1]
        if ((current[0]=='0' and len(current)>1) or int(current)>255):
            continue
        backtrack(ip_address[i+1:], segments + [ip_address[:i+1]])

res = []
backtrack(ipAddress,[])
print(res)






    

        