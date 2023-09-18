n=int(input())
v=int(input())
s=0
p=0
for i in range(1,n):
    if n%i==0:
        s=s+i
for j in range(1,v):
    if v%j==0:
        p=p+j
if n==p and v==s:
    print("Amicable")
else:
    print("Not Amicable")