import math
N = int(input("Enter the number: "))

def minSquares(N):
    dp = [float('inf')]* (N+1)
    dp[0] = 0
    # dp gets filled with the answer to the ith number 
    for i in range(1, N+1):
        j = 1
        # just check the minimum square less than the current val and it's number of squares
        while j*j <= i:
            dp[i] = min(dp[i], dp[i- j*j]+1)
            j+=1
    print(dp)
    return dp[N]

print(minSquares(N))




