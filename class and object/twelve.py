from abc import ABC, abstractmethod
class emp(ABC):
    def empdetails(self,id, name, salary):
        print("this is an abstract class")
class emp1(emp):
    def empdetails(self,id):
        print("emp_id is 12345")
class emp2(emp):
    def emodetails(self,name):
        print(" this is name")

em = emp1()
em1 = emp2() 
em1.emodetails(name = "birai")
em.empdetails(id)