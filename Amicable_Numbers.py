n=int(input())
s=int(input())
su=0
so=0
for i in range(1,n):
    
    if n%i==0:
        su += i
for k in range(1,s):
    if s%k==0:
        so += k
if n==so and s==su:
    print("Amicable")
else:
    print("Not Amicable")
    
    