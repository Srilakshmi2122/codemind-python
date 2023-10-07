def Adam(n):
    s=0
    while n:
        r=n%10
        n=n//10
        s=s*10+r
    return s
n=int(input())
sq=n*n
rev=Adam(n)
sq1=rev*rev
if sq==Adam(sq1):
    print(True)
else:
    print(False)