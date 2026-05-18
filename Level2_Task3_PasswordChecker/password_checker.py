def password_strength(password):
    length = len(password)

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong Password"

    elif length >= 6 and (has_upper or has_lower) and has_digit:
        return "Medium Password"

    else:
        return "Weak Password"


pwd = input("Enter your password: ")
print(password_strength(pwd))