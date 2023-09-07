def rev(a):
    s=0
    t=-a if a<0 else a
    while t:
        r=t%10
        s=s*10+r
        t=t//10
    if a>0:
        return s
    else:
        return -s
n=int(input())
print(rev(n))