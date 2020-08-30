import random
from datetime import datetime 


#	Let's start with the classes for different non liquid investments.
#		The question asks for inheritence. So let's create one: 

class NonLiquidItems():
	def __init__(self, value, name):
		self.name = name
		self.value = value

class Stock(NonLiquidItems):
	def __init__(self, value, name):
		NonLiquidItems.__init__(self, int(value), name)

class MutualFund(NonLiquidItems):
	def __init__(self, name):
		NonLiquidItems.__init__(self, float(1), name)

class Bond(NonLiquidItems):
	def __init__(self, value, name):
		NonLiquidItems.__init__(self, int(value), name)


#	Let's continue with our Portfolio class where we have
#		1) cash attitude
#		2) stock value attitude
#		3) mutual_funds value attitude
	

class Portfolio():
	def __init__(self):
		self.cash = float(0)
		self.item_dictionary = {}
		self.value_dictionary = {}
		self.history_string = "Here is the list of all transactions ordered by time:\n"
		#	cool! Now let's create the Porfoglio class methods for cash addition, 
		#		substraction, and the purchase of other items.

	def addCash(self, add):
		if type(add) not in [int, float]:
			raise TypeError("\nInput should be either integer or float.")
		else:
			self.cash += add
			now = datetime.now() 
			date_time = now.strftime("%d/%m/%Y at %H:%M:%S.%f")
			output = "{} unit cash is deposited. Current deposited unit cash is {}.\n".format(add, self.cash)
			self.history_string += f"{date_time},\n{output}"


	def withdrawCash(self, remove):
		if type(remove) not in [int, float]:
			raise TypeError("Input should be either integer or float.")
		elif self.cash < remove:
			raise ValueError("The amount desired to be withdrawn cannot be greater than the deposited cash.")
		else:
			self.cash -= remove
			output = "{} unit cash is withdrawm. Current deposited unit cash is {}.\n".format(remove, self.cash)
			now = datetime.now() 
			date_time = now.strftime("%d/%m/%Y at %H:%M:%S.%f")
			self.history_string += f"{date_time},\n{output}"
		#	Yes! Now let's create functions for the stock purchase and sale:

	def  buyItem(self, number, item):
		if type(number) not in [int, float]:
			raise TypeError("Stock input must be integer while mutual funds input must be float.")
		elif self.cash < number*item.value:
			raise ValueError("The desired item requires greater unit cash than the deposited cash.")
		else:
			self.withdrawCash(number*item.value)
			self.value_dictionary.update({item.name : item.value})
			if item.name in self.item_dictionary:
				dict_tempo = {"{}".format(item.name) : self.item_dictionary[item.name] + number}
				self.item_dictionary.update(dict_tempo)
			else:
				dict_tempo = {"{}".format(item.name) : number}
				self.item_dictionary.update(dict_tempo)
			output = "{} unit cash is spent to buy {} number of {}.\n".format((number*item.value), number, item.name)
			now = datetime.now() 
			date_time = now.strftime("%d/%m/%Y at %H:%M:%S.%f")
			self.history_string += f"{date_time},\n{output}"
		#	Yes! Now let's create functions for the stock purchase and sale:

	def buyStock(self, number, name):
		self.buyItem(int(number), name)

	def buyMutualFund(self, number, name):
		self.buyItem(float(number), name)

	def buyBond(self, number, name):
		self.buyItem(int(number), name)
	#Now let's update selling methods:

	def  sellItem(self, item, number, item_type):
		if type(number) not in [int, float]:
			raise TypeError("Stock input must be integer while mutual funds input must be float.")
		elif item not in self.item_dictionary:
			raise ValueError(f"You do not have any {item} to sell.")
		elif self.item_dictionary[item] < number:
			raise ValueError("You do not have enough {} unit item to sell. You can sell {} at max.".format(item, self.item_dictionary[item]))
		else:
			if item_type == "stock":
				profit = round(random.uniform(0.5*(number*portfolio.value_dictionary[item]), 1.5*(number*portfolio.value_dictionary[item])),2)
				self.addCash(profit) 
				self.item_dictionary.update({item: self.item_dictionary[item]-number})
			elif item_type == "mutualfund":
				profit = round(random.uniform(9,1.1),2)
				self.addCash(profit) 
				self.item_dictionary.update({item: self.item_dictionary[item]-number})
			elif item_type == "bond":
				profit = round(number*random.normalvariate(portfolio.value_dictionary[item], 0.1*(portfolio.value_dictionary[item])))
				self.addCash(profit) 
				self.item_dictionary.update({item: self.item_dictionary[item]-number})
			else:
				raise TypeError("Item type is not recognized. Choose either \'stock, mutualfund, or bond\'")
		output = "{} cash is earned from the sale of {} unit of {} item.\n".format(profit, number, item)
		now = datetime.now() 
		date_time = now.strftime("%d/%m/%Y at %H:%M:%S.%f")
		self.history_string += f"{date_time},\n{output}"
	# Let's create the selling functions:
	
	def sellStock(self, item, number):
		self.sellItem(item, int(number), item_type = "stock")

	def sellMutualFund(self,  item, number):
		self.sellItem(item, float(number), item_type = "mutualfund")

	def sellBond(self, item, number):
		self.sellItem(item, int(number), item_type = "bond")
	#	Now, let's define a history method.

	def history(self):
		print(self.history_string)




portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
# portfolio.addCash("300.50") #Shouldn't add and must throw and error message. 
portfolio.withdrawCash(100.25) #Substract cash to the portfolio
portfolio.history_string
portfolio.history()

#	We also need the classes of stock and mutual funds as follows:
s = Stock(20, "HFH")
portfolio.buyStock(5, s) #	WWOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOWWWW, It works sooo good!

#	Now go over the mutual fund we created by inheritence:
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print("Cash: ", portfolio.cash, "\nAssets:", portfolio.item_dictionary)	# Cool!

#	Let's look for the sell option.
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50


#	So far great! Now, buy and some bonds. Note that, by construct, the profit of bonds are normally distributed 
#		with a mean value as purchase value and sd as the one tenth of the mean value.

b1 = Bond(10, "Gov't Bond")
portfolio.buyBond(4, b1)
print("Cash: ", portfolio.cash, "\nAssets:", portfolio.item_dictionary)	# Cool!
portfolio.sellBond("Gov't Bond", 4) #Sells 1 share of HFH



portfolio.history()#Prints a list of all transactions ordered by time