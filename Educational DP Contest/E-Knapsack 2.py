import numpy as np
N,W = map(int,input().split())
dp = np.full(N*1000+1,W+1)
dp[0] = 0
for _ in range(N):
    w,v = map(int,input().split())
    np.minimum(dp[v:],dp[:-v]+w,out = dp[v:])
print(np.where(dp<=W)[0][-1])
