def add(a,b):
    add=a+b
    print(str(a) + " + " + str(b) +" = " + str(add))
def sub(a,b):
    sub=a-b
    print(str(a) + " - " + str(b) +" = " + str(sub))
def mult(a,b):
    mult=a*b
    print(str(a) + " * " + str(b) +" = " + str(mult))
def div(a,b):
    try:
        div=a /b
        print(str(a) + " / " + str(b) +" = " + str(div))
    except:
        print("Divisor cannot equal zero.")

while True:

    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplicaiton")
    print("D. Division")
    print("E. Exit")

    choice= input("your choice of action: ")

    choice=choice.lower()

    if choice== "a":
        a=int(input("first number: "))
        b=int(input("second number: "))
        add(a,b)
    elif choice== "b":
        a=int(input("first number: "))
        b=int(input("second number: "))
        sub(a,b)
    elif choice== "c":
        a=int(input("first number: "))
        b=int(input("second number: "))
        mult(a,b)
    elif choice== "d":
        a=int(input("first number: "))
        b=int(input("second number: "))
        div(a,b)
    else:
        print("program ended")
        quit()