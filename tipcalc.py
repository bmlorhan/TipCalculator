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


def tip(r):
	tr = {1: .1, 2: .13, 3: .15, 4: .17, 5: .2}  #
	tp = tr[r]  # Tip percentage
	
	return tp


def gbill(b, r):    # Group bill
	t = b + (b * tip(r))  # Total after the bill and tip are added together
	
	return t


def ibill(d, r):    # Individual bill
	t = d + (d * tip(r))  # Total after the dish and tip are added together
	
	return t


def etip(b):
	p = int(input("How many people are paying? "))  #
	b /= p
	r = int(input("On a scale of 1 - 5, how would you rate your service? "))
	print("Each person is responsible for " + format(gbill(b, r), '.2f'))  # outputs information


def itip(b, bt):
	while bt > 0:
		
		d = float(input("Enter dish price: "))
		r = int(input("On a scale of 1 - 5, how would you rate your service? "))
		bt = bt - d
		
		print("This person is responsible for:  " + format(ibill(d, r), '.2f'))  # outputs information
		
		if bt <= 0:
			print("Your grand total is: " + format(ibill(b, r), '.2f'))
			break


def main():
	try:
		b = float(input("What is your subtotal? "))  # gets subtotal of Bill.
		s = input("Are you splitting the bill? ")    # Split bill?
		
		if s == "yes" or s == "y":
			e = input("Will it be split equally? ")  # Equal split or individual?
			
			if e == "yes" or e == "y":
				etip(b)
				
			elif e == "no" or e == "n":
				bt = b
				itip(b, bt)
						
		elif s == "no" or s == "n":
			pass
		
		else:
			pass
	
	except ValueError:
		print("Please enter a number")
	

main()
