import random

#	Let's start with the classes for different non liquid investments.
#		The question asks for inheritence. So let's create one: 

class NonLiquidItems():
	def __init__(self, value, name):
		self.name = name
		self.value = value

class Stock(NonLiquidItems):
	def __init__(self, value, name):
		NonLiquidItems.__init__(self, value, name)

class MutualFund(NonLiquidItems):
	def __init__(self, name):
		NonLiquidItems.__init__(self, float(1), name)


#	Let's continue with our Portfolio class where we have
#		1) cash attitude
#		2) stock value attitude
#		3) mutual_funds value attitude

class Portfolio():
	def __init__(self):
		self.cash = float(0)
		self.stock_dictionary = {}
		self.mutualfunds_dictionary = {}
		#	cool! Now let's create the Porfoglio class methods for cash addition, 
		#		substraction, and the purchase of other items.

	def addCash(self, add):
		if type(add) not in [int, float]:
			raise TypeError("\nInput should be either integer or float.")
		else:
			self.cash += add
			print("""\n{} unit cash is deposited.\nCurrent deposited unit cash is {}.""".format(add, self.cash))

	def withdrawCash(self, remove):
		if type(remove) not in [int, float]:
			raise TypeError("Input should be either integer 			or ValueError.")
		elif self.cash < remove:
			raise ValueError("The amount desired to be withdrawn cannot be greater than the deposited cash.")
		else:
			self.cash -= remove
			print("""\n{} unit cash is withdrawm.\nCurrent deposited unit cash is {}.""".format(remove, self.cash))
		#	Yes! Now let's create functions for the stock purchase and sale:

	def  buyStock(self, number, stock):
		if type(number) not in [int]:
			raise TypeError("Input should be integer.")
		elif self.cash < number*stock.value:
			raise ValueError("The amount desired to be used to purchase stocks cannot be greater than the deposited cash.")
		else:
			self.withdrawCash(number*stock.value)
			if stock.name in self.stock_dictionary:
				dict_tempo = {"{}".format(stock.name) : number + self.stock_dictionary[stock.name]}
				self.stock_dictionary.update(dict_tempo)
			else:
				dict_tempo = {"{}".format(stock.name) : number}
				self.stock_dictionary.update(dict_tempo)				
			print("""\n{} unit cash is spent to buy {} number of {} stock.""".format((number*stock.value), number, stock.name))
		#	Yes! Now let's create functions for the stock purchase and sale:


portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
# portfolio.addCash("300.50") #Shouldn't add and must throw and error message. 
portfolio.withdrawCash(100.25) #Substract cash to the portfolio

#	We also need the classes of stock and mutual funds as follows:
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
portfolio.buyStock(5, s) #	IT WORKS



	def  sellStock(self, stock, number):
		if type(number) not in [int]:
			raise TypeError("Input should be integer.")
		elif self.cash < number*stock.value:
			raise ValueError("The amount desired to be used to purchase stocks cannot be greater than the deposited cash.")
		else:
			profit = random.uniform(0.5*(number*stock.value), 1.5*(number*stock.value))
			self.addCash(profit)
			self.stock_value -= number*stock.value
		print("""\n{} cash is earned from the sale of {} number of {} stock.""".format(profit, number, stock.name))
		#	Yes! Now let's create functions for the stock purchase and sale:

new_dict = {**dict, **{'c': 3}}


stock_dictionary = {'A': 5}

	#	Let's try this:
portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
# portfolio.addCash("300.50") #Shouldn't add and must throw and error message. 
portfolio.withdrawCash(100.25) #Substract cash to the portfolio

#	We also need the classes of stock and mutual funds as follows:
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
portfolio.sellStock("HFH", 1)


mf1 = MutualFund("BRT")