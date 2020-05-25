import sys
sys.setrecursionlimit(10000000)
def dfs(node,paths,dp,vis):
    vis[node]=True
    for i in range(0, len(paths[node])):
        if not vis[paths[node][i]]:
            dfs(paths[node][i],paths,dp,vis)
        dp[node]=max(dp[node],1+dp[paths[node][i]])
n,m=map(int,input().split())
paths=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    paths[a].append(b)
dp,vis=[0]*(n+1),[False]*(n+1)
for i in range(1,n+1):
    if not vis[i]:
        dfs(i,paths,dp,vis)
print(max(dp))
