#!/usr/bin/env python3
# Created by: Adrian Student
# Date : 26th sept 2026
# this programs asks the user for the diameter of the
# pizza and then calculate and display the prize of
# the pizza with taxes.
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = (
        constants.LABOUR_cost
        + constants.RENTAL_cost
        + constants.INGREDIENTS_cost * diameter
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # output
    print("")
    print("total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
