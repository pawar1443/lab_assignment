# Sample temperatures for 10 cities
fahrenheit_temps = [86, 77, 90, 68, 72, 85, 79, 88, 95, 80]  # Fahrenheit values
celsius_temps = [30, 25, 32, 20, 22, 29, 26, 31, 35, 27]     # Celsius values

# Lambda function to convert Fahrenheit to Celsius
f_to_c = lambda f: (f - 32) * 5 / 9

# Lambda function to convert Celsius to Fahrenheit
c_to_f = lambda c: (c * 9 / 5) + 32

# Convert all Fahrenheit temps to Celsius using map
converted_to_celsius = list(map(f_to_c, fahrenheit_temps))

# Convert all Celsius temps to Fahrenheit using map
converted_to_fahrenheit = list(map(c_to_f, celsius_temps))

print("Fahrenheit to Celsius:", converted_to_celsius)
print("Celsius to Fahrenheit:", converted_to_fahrenheit)
