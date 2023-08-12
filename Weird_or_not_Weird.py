x=int(input())
if(x%2==0):
    if x>=2 and x<=5:
        print("not weird")
    if x>=6 and x<=20:
        print("weird")
    if x>20:
        print("not weird")
else:
    print("weird")