class checknum (Exception):
  pass
class smaller (checknum):
  pass
class larger (checknum):
  pass

num = 52
try:
  number = int(input("Enter the number to compare : "))
  if number < num:
    raise smaller ("number is smaller.")
  elif number > num:
    raise larger ("number is larger.")
except smaller as e:
    print(e)
except larger as e:
    print(e)
else:
    print("Number is equal to ",num)