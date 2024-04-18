password = input("Enter new password")

result = {}

if len(password) > 7:
    result["lenght"] = True
    print("Great password there")

elif len(password) == 7:
    result["lenght"] = True
    print("Password is OK, but not too strong")
else:
    result["lenght"] = False
    print("Your password is weak")