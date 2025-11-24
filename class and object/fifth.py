class sum:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
        self.ans = self.num1 + self.num2

    def calsum(self):
        return self.ans
obj = sum(20,30)
print(obj.calsum())