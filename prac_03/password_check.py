MIN_LENGTH = 10


def main():
    valid_password = get_password()
    display_password(valid_password)


def get_password():
    password = input("Enter password (min. 10 characters): ")
    while len(password) < MIN_LENGTH:
        print("Password is too short")
        password = input("Enter password (min. 10 characters): ")
    return password


def display_password(password):
    print("*" * len(password))


main()
