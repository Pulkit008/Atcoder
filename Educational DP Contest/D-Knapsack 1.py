"""
n,w=map(int,input().split())
wv=[list(map(int,input().split())) for _ in range(n)]
wv.sort()
cost=[[0]*(w+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(w+1):
        if wv[i-1][0] <= j:
            cost[i][j]=max(wv[i-1][1]+cost[i-1][j-wv[i-1][0]],cost[i-1][j])
        else:
            cost[i][j]=cost[i-1][j]
print(cost[n][w])
"""

import numpy as np
n,w=map(int,input().split())
dp=np.zeros(w+1,dtype=np.int64)
for _ in range(n):
    we,v=map(int,input().split())
    np.maximum(dp[we:],dp[:-we]+v,out = dp[we:])
print(dp[w])
