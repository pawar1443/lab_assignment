class emplyee():
    def __init__(self,name,age,id,salary):
        self.Name = name
        self.Age = age
        self.Id=id
        self.Salary = salary

n = int(input("how many emp you want"))
for i in range(1,n+1):
    name = input("enter your name : ")
    age = int(input("enter age : "))
    id = int(input("enter id : "))
    salary = int(input("enter your salary : "))

    