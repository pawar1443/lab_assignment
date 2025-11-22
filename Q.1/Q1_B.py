def cal():
    pro = 1
    sum = 0
    list = [1,2,3,4,5,6,7,8,9,10]
    for i in list:
        if i % 2 == 0:
            pro *= i
        else:
            sum += i
        
    print(pro)
    print(sum)

cal()
