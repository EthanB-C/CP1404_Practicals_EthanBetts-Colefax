"""CP1404 Emails"""


def main():
    emails_dict = {}
    email = input("Email: ")
    while email != '':
        name = create_name(email)
        is_name = input(f"Is yor name {name}? (Y/N) ").lower()
        if is_name in ['y', 'yes', '']:
            emails_dict[email] = name
            email = input("email: ")
        elif is_name in ['n', 'no']:
            name = input("Name: ")
            emails_dict[email] = name
            email = input("Email: ")
        else:
            print("Invalid choice")
    display_name_and_email(emails_dict)


def create_name(email):
    name = email.split('@')[0].replace('.', ' ').title()
    return name


def display_name_and_email(emails_dict):
    print("")
    for email, name in emails_dict.items():
        print(f"{name} ({email})")


main()
