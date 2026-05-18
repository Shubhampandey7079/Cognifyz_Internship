def is_palindrome(text):
    text = text.lower()  # case insensitive
    return text == text[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")