string = input("Enter a string: ")

# If length is odd → cannot be symmetrical
if len(string) % 2 != 0:
    print("The string is NOT Symmetrical")
else:
    mid = len(string) // 2
    first_half = string[:mid]
    second_half = string[mid:]

    if first_half == second_half:
        print("The string IS Symmetrical")
    else:
        print("The string is NOT Symmetrical")
