N=int(input())
C=[0]*4
for i in map(int, input().split()):
    if i==1:
        C[1]+=1
    elif i==2:
        C[2]+=1
    else:
        C[3]+=1
dp = [[[.0] * (N + 2) for _ in range(N + 2)] for _ in range(N + 2)]
for i in range(C[3] + 1):
    for j in range(N - C[1] - i + 1):
        for k in range(N - i - j + 1):
            if i + j + k != 0:
                dp[i][j][k] = (
                    N +
                    i * dp[i - 1][j + 1][k] +
                    j * dp[i][j - 1][k + 1] +
                    k * dp[i][j][k - 1]
                ) / (i + j + k)
print(dp[C[3]][C[2]][C[1]])
