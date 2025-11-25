class person:
    def __init__(self,name):
        self.name=name
    def hello(self):
        print("hello my name is : ",self.name)
p = person("neha")
p.hello()
