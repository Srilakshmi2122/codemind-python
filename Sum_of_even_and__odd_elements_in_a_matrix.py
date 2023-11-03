r,c =map(int,input().split())
mat = []
for i_list in range(r):
    i_list = list(map(int,input().split()))
    mat.append(i_list)
s = 0
s1 = 0
for i_list in mat:
    for i in i_list:
        if i%2==0:
            s += i
        else:
            s1 += i
print(s,s1)