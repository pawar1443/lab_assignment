try:
    f = open("my.txt" , "r")
    data = f.read()
    print(data)
except IOError:
    print("Error : this file cannot be open or it dosent exist")