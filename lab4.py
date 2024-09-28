x=int(input("number: "))
y=x<<1
if y!=0:
    print(y)
else:
    print("nenu")
x=int(input("number: "))
y=int(input("num2: "))
m=str(input("*, /, +, -, "))
if m ==("*"):
    print(x*y)
if m ==("/"):
    print(x/y)
    if m == ("+"):
        print(x + y)
        if m == ("-"):
            print(x - y)
x=input("num: ")
if len(x)==4:
    y=int(x)
    z=y//1000
    m=(y%1000)//100
    n=((y%1000)%100)//10
    t=(((y%1000)%100)%10)
    if (z+t)==(m+n):
        print("yes")
    else:
        print("no")

x=int(input("num: "))
if x>=18:
    print("acsess")
else:
    print("not acsess")

x=int(input("number: "))
y=int(input("num2: "))
m=int(input("num3: "))
if x+1==y:
    if y+1==m:
        print("yes")
x=int(input("number: "))
y=int(input("num2: "))
m=int(input("num3: "))
if x+1==y:
    if y+1==m:
        print("yes")

