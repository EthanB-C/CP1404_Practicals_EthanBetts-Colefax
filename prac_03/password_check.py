MIN_LENGTH = 10
password = input("Enter password (min. 10 characters): ")
while len(password) < MIN_LENGTH:
    print("Password is too short")
    password = input("Enter password (min. 10 characters): ")
print("*" * len(password))

