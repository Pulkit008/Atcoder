n,l=int(input()),list(map(float,input().split()))
dp=[[0.0]*(n+1) for _ in range(n+1)]
dp[0][0]=1.0
for i in range(1,n+1):
    for j in range(i+1):
        if j==0:
            dp[i][j]=dp[i-1][j]*(1.0-l[i-1])
        else:
            dp[i][j]=dp[i-1][j]*(1.0-l[i-1])+dp[i-1][j-1]*l[i-1]
print(sum(dp[n][((n+1)//2):]))

"""
from numpy import zeros
 
N = int(input())
P = map(float, input().split())
 
dp = zeros(N + 1)
dp[0] = 1.0
 
for p in P:
    T = dp
    dp = T * (1 - p)
    dp[1:] += T[:-1] * p
 
print(dp[-(-N // 2):].sum())"""
