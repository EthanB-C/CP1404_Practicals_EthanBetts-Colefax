"""My Guitars Program"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    my_guitars = []
    guitar = get_guitar()
    while guitar != '':
        my_guitars.append(guitar)
        guitar = get_guitar()
    display_my_guitars(my_guitars)


def get_guitar():
    name = input("Name: ")
    if name == '':
        return ''
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    cost = round(cost, 2)
    guitar = Guitar(name, year, cost)
    print(guitar, "added.\n")
    return guitar


def display_my_guitars(my_guitars):
    guitar_number = 0
    print("These are my guitars:")
    for guitar in my_guitars:
        guitar_number += 1
        guitar_vintage = '(vintage)' if guitar.is_vintage() is True else ''
        print(f"Guitar {guitar_number}: {guitar.name:>20}, worth ${guitar.cost:10,.2f} {guitar_vintage}")


main()
