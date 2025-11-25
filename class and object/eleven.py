class employee(object):
    def __init__(self):
        self.name = 1234
        self._age = 1234
        self.__salary = 20000
    def publicFun(self):
        print(self.__salary)
emp = employee()
print(emp.name)
print(emp._age)
emp.publicFun()