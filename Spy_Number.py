n=int(input())
s=0
p=1
while True:
    r=n%10
    s=s+r
    p=p*r
    n=n//10
    if n==0:
        break
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")