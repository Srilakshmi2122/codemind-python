n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    temp=i
    while temp:
        d=temp%10
        if d==0:
            break
        if i%d!=0:
            break
        temp=temp//10
    else:
        print(i,end=" ")