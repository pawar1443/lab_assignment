try:
    f = open("myfile.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("Error: File does not exist.")
