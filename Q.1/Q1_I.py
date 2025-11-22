def swAp(lsT , i , j):
    lsT[i] , lsT[j] = lsT [j] , lsT[i]
    return lsT

lst = [1,2,3,4]
print(swAp(lst , 1 , 2))