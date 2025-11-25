# father -> son  (single)
#father(parent)
#child/son (derived)

class emp:
    def _init_(self,name,age,salary):
        self.Name=name
        self.Age=age
        self.Sal=salary
    def hello(Self):
        print("Hello")
class empchild(emp):
    def _init_(self, name, age, salary,id):
        self.ID=id
        emp._init_(self,name,age,salary)

emp1=empchild('Radhika',20,20000,229)
emp1.hello()
print(emp1._dict_)