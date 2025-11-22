class number (Exception):
    pass
class odd (number):
    pass
class even (number):
    pass

try:
    num = int(input("enter a number : "))

    if num % 2 == 0 and num > 0:
        raise even("the number is even ")
    elif num % 2 != 0 and num > 0 :
        raise odd("the number is odd")
    
except even as e:
    print(e)
except odd as e:
    print(e)
else:
    print("number is zero")