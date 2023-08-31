x,a,b=map(int,input().split())
k=a*b
if x%k==0:
    print(x//k)
else:
    print(x//k+1)