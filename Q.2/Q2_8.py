from functools import *
lst = []
how = int(input("how many numbers you want to add : "))

for i in range(1,how +1):
    n = int(input("enter number : "))
    lst.append(n)


if how > 3:
    print(lst)
    result = sum(filter(lambda x : x % 2 == 0 , lst))
    print(result)
    result2 = reduce(lambda a,b : a*b , filter(lambda x : x % 2 != 0 , lst) , 1)
    print(result2)
else:
    print(lst)
