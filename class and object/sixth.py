class fact:
    def __init__(self,n):
        self.n = n
    def calfact(self):
        fact = 1
        for i in range(1,self.n+1):
            fact *= i
        return fact
    
obj = fact(5)
print(obj.calfact())