num=int(input())
sq=num**2
n=len(str(num))
last = sq%pow(10,n)
if last==num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")