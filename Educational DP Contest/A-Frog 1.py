"""
n,l=int(input()),list(map(int,input().split()))
c1,c2=0,abs(l[0]-l[1])
for i in range(2,n):
  t=c2
  c2=min(c1+abs(l[i]-l[i-2]),c2+abs(l[i]-l[i-1]))
  c1=t
print(c2)

"""



n,l=int(input()),list(map(int,input().split()))
c=[0]*n
c[1]=abs(l[0]-l[1])
for i in range(2,n):
  c[i]=min(c[i-2]+abs(l[i]-l[i-2]),c[i-1]+abs(l[i]-l[i-1]))
print(c[-1])
