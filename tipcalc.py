# Tip Calculator v2.0
# February 26th, 2017
#
#
# User enters the total bill and the tip percentage, calculates the new total
# bill + tip% = total
#
# TODO:
# Split bill: add feature to allow input of unique and independent bills.
# example: total bill is 100, A is paying 30 and B is paying 70. Calculate two tip totals separately and include
#   a complete total. example cont.: A pays 35 and B pays 81 for a total of 116.


def tip(r):

    s = {1: .1, 2: .13, 3: .15, 4: .17, 5: .2}
    t = s[r]

    return t


def main():
    try:
        b = float(input("What is your bill? "))
        s = input("Are you splitting the bill? ")
        if s == "yes" or s == "y":
            e = input("Will it be split equally? ")
            if e == "yes" or e == "y":
                c = int(input("How many times? "))
                b /= c
            elif e == "no" or e == "n":
                i = input("How many items? ")
                print(i)
        elif s == "no" or s == "n":
            pass
        else:
            pass
        r = int(input("On a scale of 1 - 5, how would you rate your service? "))
    except ValueError:
        print("Please enter a number")

    total = b + (b * tip(r))

    print("Your total bill is " + format(total, '.2f'))

main()
