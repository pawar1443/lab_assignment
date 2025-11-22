num = int(input("Enter a number: "))

temp = num         
sum_of_power = 0   
count = 0

n = temp
while n > 0:
    count += 1
    n = n // 10

n = temp
while n > 0:
    digit = n % 10
    sum_of_power += digit ** count
    n = n // 10

if sum_of_power == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
