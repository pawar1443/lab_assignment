def fib(num):
    a=0
    b=1
    for i in range(num):
        print(a , end = " ")
        temp = a
        a = b
        b = temp + b

n = int(input("enter a number : "))
fib(n)

