lst = [2,1,4,1,2]
uni = []

for i in lst:
    if i not in uni:
        uni.append(i)

l,r = 0, len(uni)-1

while l<r:
    uni[l],uni[r] = uni[r],uni[l]
    l+=1
    r-=1
print(uni)
