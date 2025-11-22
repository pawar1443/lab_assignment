try:
    lst = [1,2,3,4,5]
    num = int(input("enter value : "))
    print(lst[num])
except IndexError:
    print("index out fo bound ")
