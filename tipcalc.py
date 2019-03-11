# Tip Calculator v2.0
# February 26th, 2017
#
#
# User enters the total bill and the tip percentage, calculates the new total
# bill + tip% = total
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


def splitBill(split):
    try:
        choices = ["yes", "no"]
        if split == choices[0]:
            bill = float(input("What is your bill? "))  # User inputs bill total.
            equal = input("Will it be split equally? ")  # Equal split or individual?

            if equal == choices[0]:
                equalTip(bill)

            elif equal == choices[1]:
                bill_total = bill
                individualTip(bill, bill_total)

        if split == choices[1]:
            bill = float(input("What is your bill? "))  # User inputs bill total.
            bill_total = bill
            individualTip(bill, bill_total)

        if split != choices[0] and split != choices[1]:
            print("Please enter a (Y)es or (N)o.")
            main()
        else:
            quit()

    except ValueError:
        print("Please enter a number")
        splitBill(split)


def main():

        split = input("Are you splitting the bill? ")  # Split bill?
        splitBill(split)


main()
