n=int(input())
a,b,c=map(int,input().split())
for _ in range(1,n):
    aa,bb,cc=map(int,input().split())
    a,b,c=aa+max(b,c),bb+max(a,c),cc+max(a,b)
print(max(a,b,c))
