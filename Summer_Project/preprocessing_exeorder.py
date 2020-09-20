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

os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020/Summer_Project/')

##
##
##	Let's open Tweets and Order as dataframes: 
data_ExecOrders = pd.read_csv("gencer_exeorder.csv") 
data_ExecOrders.head()
data_TrumpTweets = pd.read_csv("gencer_TrumpTweets.csv", sep = ",", engine='python')
data_TrumpTweets.head()
##	Looks great!

##
##
##	Let's tag tweets that explicitly say "executive order" or "order".
##		To achieve that, let's create a function for convenience:

def my_fun_finder(row):
	if row["text"].find(my_word) != -1:
		val = 1
	else:
		val = 0
	return val

##	Let's define the words we want to use:
word_list = ["executive order", "executive", "order", "unilateral", "executive action"]

##	Let's save these
for i in word_list:
	my_word = i
	data_TrumpTweets[i] = data_TrumpTweets.apply(my_fun_finder, axis=1)



data_TrumpTweets.to_csv(r'C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020/Summer_Project/gencer_TrumpTweets_2.csv')
