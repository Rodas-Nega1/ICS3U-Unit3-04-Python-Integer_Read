# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sept 2021
# This program checks a user's integer value


def main():
    # this function checks if an integer is positive, negative, or a zero

    # input
    number = int(input("Enter your integer: "))
    print("")

    # process & output
    if number > 0:
        print("{0} is positive.".format(number))

    elif number < 0:
        print("{0} is negative.".format(number))

    else:
        print("{0} is a zero.".format(number))

    print("\nDone.")


if __name__ == "__main__":
    main()
