h,w=map(int,input().split())
l=[[1 if i=='.' else 0 for i in input()] for _ in range(h)]
for i in range(w):
    if l[0][i]==0:
        for j in range(i+1,w):
            l[0][j]=0
        break
for i in range(h):
    if l[i][0]==0:
        for j in range(i+1,h):
            l[j][0]=0
        break
for i in range(1,h):
    for j in range(1,w):
        if l[i][j]!=0:
            l[i][j]=l[i-1][j]+l[i][j-1]
print(l[h-1][w-1]%(10**9+7))
