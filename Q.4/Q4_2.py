class number(Exception):
    pass
class prime(number):
    pass
class noPrime(number):
    pass

try:
    num = int(input("enter a number : "))
    count = 0
    if num == 0 or num == 1:
        print("number is not a prime")
    elif num > 0:
        for i in range(1,num+1):
            if num % i == 0:
                count +=1
        if count == 2:
            raise prime("the numebr is prime")
        else:
            raise noPrime("The number is not a prime")
except prime as e:
    print(e)
except noPrime as e:
    print(e)
else:
    print("please enter possitive number")
        