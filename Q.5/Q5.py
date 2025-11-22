def rage():
  age = int(input("Enter age = "))
  if(age <0 or age>130):
    raise ValueError
    print("yout age is : " , age)
  return age

try:
  age = rage()
  print("your age is : ",age)
except ValueError:
  print("Age is Invalid")
else:
  print("No Exception")