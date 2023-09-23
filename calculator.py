print("1: Add\n2: Subtract\n3: Multiply\n4: Divide")
c = int(input("Enter choice: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if(c==1):
    print(a+b)
elif c==2:
    if(a>b):
        print(a-b)
    else:
        print(b-a)
elif c==3:
    print(a*b)
else:
    print(float)(a/b)
print("by Aruf")
