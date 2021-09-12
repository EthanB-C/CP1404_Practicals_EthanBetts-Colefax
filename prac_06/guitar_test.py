"""Guitar test program for Guitar Class"""

from prac_06.guitar import Guitar

guitar1 = [Guitar("Gibson L-5 CES", 1922, 16035.40), 99, True]
guitar2 = [Guitar("Another Guitar", 2013), 8, False]


def main():
    print("{} get_age() - Expected {}. Got {}".format(guitar1[0].name, guitar1[1], guitar1[0].get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar1[0].name, guitar1[2], guitar1[0].is_vintage()))


main()
