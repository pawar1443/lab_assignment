class emp:
    def __init__(self,name,age,salary):
        self.Name=name
        self.Age=age
        self.Sal=salary
    def hello(Self):
        print("Hello")

class emp1(emp):
    def __init__(self, name, age, salary,id):
        self.ID=id
        emp.__init__(self,name,age,salary)
    def msg(self):
        print("this is a parent class")

class empchild(emp1):
    def __init__(self,name,age,salary,email):
        self.email = email
        emp1.__init__(self,name,age,salary,id)

em=empchild('Radhika',20,20000,229)
em.msg()
em.hello()
print(em.__dict__)


