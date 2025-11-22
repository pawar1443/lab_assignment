def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

string = input("Enter a string: ")

if is_palindrome(string):
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
