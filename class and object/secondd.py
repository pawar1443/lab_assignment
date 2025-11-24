class person():
    a = 10
    print("hello")
    def __init__(self):
        print("hi")
    def display(self):
        print("welcome")

p = person()
print(p.a)
print(p.display())