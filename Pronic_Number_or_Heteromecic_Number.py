n=int(input())
flag = False
for i in range(1,n):
    b=i*(i+1)
    if n==b:
        flag=True
        break
    else:
        flag=False
if flag==True:
    print("YES")
else:
    print("NO")