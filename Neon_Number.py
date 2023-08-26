n=int(input())
k=n*n
q=k
s=0
while q>0:
    r=q%10
    s=s+r
    q=q//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")