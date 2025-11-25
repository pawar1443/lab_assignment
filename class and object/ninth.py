class employee:
    empcount = 0
    empsalary = 0

    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
        employee.empcount = employee.empcount+1
        employee.empsalary = employee.empsalary + self.salary

    def displaycount(self):
        print("total Employee %d",employee.empcount)

    def displayamount(self):
        print("Total salary %d", employee.empsalary)

    def displayemp(self):
        print(" ID : ",self.id," Name : ",self.name," Salary : ",self.salary)

emp1 = employee(201,"Neha",20000)
emp2 = employee(202,"Sharadha",50000)

emp1.displaycount()
emp1.displayamount()
emp1.displayemp()