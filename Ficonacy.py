x=int(input("Quantos termos voce quer mostrar? "))
i=0
h=1
print("{}→{}→".format(i,h),end="")
while x>0:
    r=i+h
    print("{}→".format(r),end="")
    i=h
    h=r
    x-=1
print("∞")