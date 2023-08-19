a,b,c=map(int,input().split())
if a>c and b>c:
    print(f"{a+b}")
elif b>a and c>a:
    print(f"{b+c}")
else:
    print(f"{a+c}")