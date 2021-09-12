"""Guitar test program for Guitar Class"""

from prac_06.guitar import Guitar

guitar1 = [Guitar("Gibson L-5 CES", 1922, 16035.40), 99, True]
guitar2 = [Guitar("Another Guitar", 2013), 8, False]
guitars = [guitar1, guitar2]


def main():
    for guitar in guitars:
        print("{} get_age() - Expected {}. Got {}".format(guitar[0].name, guitar[1], guitar[0].get_age()))
        print("{} is_vintage() - Expected {}. Got {}".format(guitar[0].name, guitar[2], guitar[0].is_vintage()))


main()
