def is_valid_email(email):
    if "@" in email and "." in email:
        at_index = email.index("@")
        dot_index = email.rindex(".")

        # basic checks
        if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
            return True
    return False


user_email = input("Enter email address: ")

if is_valid_email(user_email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")