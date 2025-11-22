from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square each number using map and lambda
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Filter out even numbers using filter and lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd_numbers)

# Find the sum of all numbers using reduce and lambda
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)
