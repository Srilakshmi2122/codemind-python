def palin(n):
    s=0
    q=n
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    if q==s:
        print(True)
    else:
        print(False)
num=int(input())
palin(num)