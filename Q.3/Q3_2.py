try:
    a = int(input("enter a  number : "))
    b = int(input("enter second number : "))
except ValueError:
    print("please enter only interger")
else:
    print(a+b)
    print(a*b)
    print(a - b)