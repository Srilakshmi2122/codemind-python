r = int(input())   #reading rows and columns
mat1 = []
mat2 = []
for i in range(r):
    f_list = list(map(int,input().split()))
    mat1.append(f_list)
for j in range(r):
    s_list = list(map(int,input().split()))
    mat2.append(s_list)
a = []
for n in range(r):
    p=[]
    for s in range(r):
        d = abs((mat1[n][s])-(mat2[n][s]))
        p.append(d)
    a.append(p)
for k in a:
    print(*k)