############################################################################################
####								  PYTHON PROJECT									####
####								Alper Sukru Gencer 									####
############################################################################################


##	GOALs:
##	
##	
## 	Preprocessing the Orders to Prepare it for the Analysis.
## 	Preprocessing the Orders to Prepare it for the Analysis.

from bs4 import BeautifulSoup
import re 
import tweepy
import sys # add directory to system PATH
import os
import io
import csv
import pandas as pd 
import numpy as np
import datetime


os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020/Summer_Project/')

##
##
##	Let's open Tweets and Order as dataframes: 
data_ExecOrders = pd.read_csv("gencer_exeorder.csv",  engine='python') 
data_ExecOrders.head()
data_ExecOrders 
data_TrumpTweets = pd.read_csv("gencer_TrumpTweets.csv", sep = ",", engine='python')
data_TrumpTweets.head()
for col in data_TrumpTweets.columns:
	print(col)								##	Looks great!


##
##
##
##	Let's tag tweets that explicitly say "executive order" or "order".
##		To achieve that, let's create a function for convenience:

def my_fun_finder(row):
	if str(row["text"]).find(my_word) != -1:
		val = 1
	else:
		val = 0
	return val

##	Let's define the words we want to use:
word_list = ["executive order", "executive", "order", "unilateral", "executive action"]


##	Let's run it:
for i in word_list:
	my_word = i
	data_TrumpTweets[i] = data_TrumpTweets.apply(my_fun_finder, axis=1)

##	Let's save these changes:
data_TrumpTweets.to_csv(r'C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020/Summer_Project/gencer_TrumpTweets_2.csv')


##
##
##	Let's tag tweets whose intervals coincide with the executive order dates:
data_TrumpTweets = data_TrumpTweets[:22727]
order_dates = list(data_ExecOrders["OrderPublishedDate"])
order_dates[1], order_dates[10]		#	It's 	"%m-%d-%Y"
data_TrumpTweets["created_date"][1]	#	It's 	"%m-%d-%Y"
order_dates2 = []
for k in order_dates:
	order_dates2.append(datetime.datetime.strptime(k, "%m/%d/%Y"))


my_intervals = ["int_1day", "int_3day", "int_5day", "int_7day", "int_11day", "int_15day"]
for i in my_intervals:
	data_TrumpTweets[i] = "0"


def my_fun_interval(row):
	if row[i] == "0":
		if (datetime.datetime.strptime(row[(int_st)], "%m/%d/%Y") <= my_date <= datetime.datetime.strptime(row[int_ed], "%m/%d/%Y")):
			val = "1"
		else:
			val = "0"
	else:
		val = "1"
	return val 


for k in order_dates2:
	my_date = k
	print(my_date)
	for i in my_intervals:
		my_int = i
		int_st = (my_int + "_beg")
		int_ed = (my_int + "_end")
		print(my_int, int_st, int_ed)
		data_TrumpTweets[i] = data_TrumpTweets.apply(my_fun_interval, axis=1)

##	Let's save these changes:
data_TrumpTweets.to_csv(r'C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020/Summer_Project/gencer_TrumpTweets_2.csv')
