# Tip Calculator v2.0
# February 26th, 2017
#
#
# User enters the total bill and the tip percentage, calculates the new total
# bill + tip% = total


def tip(r):

    s = {1: .1, 2: .13, 3: .15, 4: .17, 5: .2}
    t = s[r]

    return t


def main():
    try:
        b = int(input("What is your bill? "))
        r = int(input("On a scale of 1 - 5, how would you rate your service? "))
    except ValueError:
        print("Please enter a number")

    total = b + (b * tip(r))

    print("Your total bill is " + str(total))

main()
