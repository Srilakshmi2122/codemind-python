s1,s2,s3,s4,s5=map(int,input().split())
p=(s1+s2+s3+s4+s5)/5
if p>=90:
    print("Grade A")
elif p>=80:
    print("Grade B")
elif p>=70:
    print("Grade C")
elif p>=60:
    print("Grade D")
elif p>=40:
    print("Grade E")
elif p<40:
    print("Grade F")