from functools import *
lst = [1,-3 ,4 ,6,-2 ,-9]

result = reduce(
    lambda a,b:a*b,
    filter(
        lambda x : x > 0 , lst
    ),
    1
)
print(result)