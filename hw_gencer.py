

#	Let's start with our Portfolio class where we have
#		1) cash attitude
#		2) stock attitude
#		3) mutual_funds attitude
#		4) nonliquiditems dictonary for convience

class Portfolio():
	def __init__(self):
		self.cash = float(0)
		self.stock = 0
		self.mutual_funds = 0
		self.nonliquiditems = {'stock': {}, 'mutual_funds': {}}
		#	cool! Now let's create the Porfoglio class methods for cash addition, 
		#		substraction, and the purchase of other items.

	def addCash(self, add):
		if type(add) not in [int, float]:
			raise TypeError("Input should be either int or add.")
		else:
			self.cash += add
			print("""{} unit cash is deposited.
				\n Current deposited unit cash is {}.""".format(add, self.cash))


#	Let's try this:
portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
