# Tip Calculator v2.0
# February 26th, 2017
#
#
# User enters the total bill and the tip percentage, calculates the new total
# bill + tip% = total
#
# TODO:
#
# Inclusion of sales tax. Two ideas: Equally divide sales tax ( default for Equally split bills ). Split sales tax
#  equally among splits, regardless of what they're paying. IE. A paying 30 contributes to paying tax the same as B
#  paying 70. Second idea is to figure out sales tax for that area and add it to all items individually. IE. A and B
#  will pay 8.5%* ( variable base on location ) of their individual meals. A pays 8.5% of 30, B pays 8.5% of 70. Second
#  option will need the inclusion of the sales tax from the receipt > more input for user. May or may not be a good
#  idea. >>> User can choose how they want to handle sales tax on their own.
# ---------------------------------------------------------------------------------------------------------------
#
# UPDATE:
# Created function etip to handle Equally split bills.
#
# DONE:
# Split bill: add feature to allow input of unique and independent bills.
#
#


def tip(service_rating):
    tip_percent = {1: .1, 2: .13, 3: .15, 4: .17, 5: .2}
    tip_total = tip_percent[service_rating]  # Tip percentage

    return tip_total


def groupBill(bill, service_rating):  # Group bill
    total = bill + (bill * tip(service_rating))  # Total after the bill and tip are added together

    return total


def individualBill(dish, service_rating):  # Individual bill
    total = dish + (dish * tip(service_rating))  # Total after the dish and tip are added together

    return total


def equalTip(bill):            # Equally split tip
    group_total = int(input("How many people are paying? "))
    bill /= group_total
    service_rating = int(input("On a scale of 1 - 5, how would you rate your service? "))
    print("Each person is responsible for " + format(groupBill(bill, service_rating), '.2f'))  # outputs information


def individualTip(bill, bill_total):           # Individual tip
    charges = []
    while bill_total > 0:

        dish = float(input("Enter dish price: "))
        service_rating = int(input("On a scale of 1 - 5, how would you rate your service? "))
        bill_total = bill_total - dish
        charges.append(individualBill(dish, service_rating))

        if bill_total < 0:
            print("Entered amount was greater than " + str(bill) + ". Double check and start over.")
            break

        print("This person is responsible for:  " + format(individualBill(dish, service_rating), '.2f'))  # outputs information

        if bill_total == 0:
            print("Your grand total is: " + format(sum(charges), '.2f'))
            break

def main():
    try:
        split = input("Are you splitting the bill? ")  # Split bill?
        bill = float(input("What is your bill? "))  # User inputs bill total.
        
        if split == "yes" or split == "y":
            equal = input("Will it be split equally? ")  # Equal split or individual?

            if equal == "yes" or equal == "y":
                equalTip(bill)

            elif equal == "no" or equal == "n":
                bill_total = bill
                individualTip(bill, bill_total)

        if split == "no" or split == "n":
            bill_total = bill
            individualTip(bill, bill_total)

        else:
            pass

    except ValueError:
        print("Please enter a number")
        main()


main()
