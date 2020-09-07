###############################################################
########################	HOMEWORK	#######################	
###############################################################

##	Author: Alper Sukru Gencer
##	Start Date: September 7, 2020
##	End Date:


##	For the purposes of this exercise, we define three types of Twitter users.
##		• Layman: Users with less than 100 followers
##		• Expert: Users with 100-1000 followers
##		• Celebrity: Users with more than 1000 followers
##	Using the Twitter API, and starting with the @WUSTLPoliSci twitter user, answer
##		the following:



##	One degree of separation:
##		- Among the followers of @WUSTLPoliSci who is the most active?
##		- Among the followers of @WUSTLPoliSci who is the most popular, i.e. has
##			the greatest number of followers?
##		 -Among the friends of @WUSTLPoliSci, i.e. the users she is following, who
##			are the most active layman, expert and celebrity?
##		- Among the friends of @WUSTLPoliSci who is the most popular?
##	Two degrees of separation: For the following two questions, limit your search
##		of followers and friends to laymen and experts.
##		- Among the followers of @WUSTLPoliSci and their followers, who is the
##			most active?
##		- Among the friends of @WUSTLPoliSci and their friends, who is the most
##			active?



##
####	SOLUTION:
##



##	Getting started:
import tweepy
import importlib # to import file
import sys # add directory to system PATH
import os
import io
import csv
import pandas as pd 




##	Let's access to the API keys:
sys.path.insert(0, 'C:/Users/alper/pyex/class/')
twitter = importlib.import_module('start_twitter')
api = twitter.client

## See rate limit
limit = api.rate_limit_status()
limit.keys() ##look at dictionary's keys prepare for dictionaries all the way down

## Let's check for all limits:
limit["resources"]["tweets"].keys()

for i in limit["resources"]["tweets"].keys():
	print(limit["resources"]["tweets"][i])

#		{'limit': 180, 'remaining': 180, 'reset': 1599513355}
#		{'limit': 450, 'remaining': 450, 'reset': 1599513355}
#		{'limit': 50, 'remaining': 50, 'reset': 1599513355}
#		{'limit': 900, 'remaining': 900, 'reset': 1599513355}
#		{'limit': 50, 'remaining': 50, 'reset': 1599513355}
#		{'limit': 1800, 'remaining': 1800, 'reset': 1599513355}
#		{'limit': 900, 'remaining': 900, 'reset': 1599513355}
#		{'limit': 450, 'remaining': 450, 'reset': 1599513355}
#		{'limit': 900, 'remaining': 900, 'reset': 1599513355}
#		{'limit': 450, 'remaining': 450, 'reset': 1599513355}
#		{'limit': 450, 'remaining': 450, 'reset': 1599513355}
#		{'limit': 50, 'remaining': 50, 'reset': 1599513355}

## Create WashU PolSci user objects
wustl_polsci = api.get_user('WUSTLPoliSci')
wustl_polsci 

## Check type and methods
type(wustl_polsci)
dir(wustl_polsci)

## Follower Count:
wustl_polsci.followers_count
wustl_polsci.statuses_count

wustl_polsci_followers = wustl_polsci.followers_ids()
len(wustl_polsci_followers)		# Out[17]: 469

## Friends Count: PROBLEM
wustl_polsci_friends = wustl_polsci.friends()
len(wustl_polsci_friends)		# Out[17]: 469

##	Let's find the most active one:
follower_dictionary = {}
for i in wustl_polsci_followers:
	follower_dictionary[i] =  (api.get_user(i)).statuses_count 

wustl_polsci_mostactive = max(follower_dictionary, key=follower_dictionary.get) # ID
follower_dictionary[max(follower_dictionary, key=follower_dictionary.get)] # Number of Tweets
api.get_user(wustl_polsci_mostactive).name # Amanda Gomez


##	Let's find the most popular one:
follower_dictionary_followers = {}
for i in wustl_polsci_followers:
	follower_dictionary_followers[i] = (api.get_user(i)).followers_count

wustl_polsci_mostfollower = max(follower_dictionary_followers, key=follower_dictionary_followers.get) # ID
follower_dictionary_followers[max(follower_dictionary_followers, key=follower_dictionary_followers.get)] # Number of Tweets
api.get_user(wustl_polsci_mostfollower).name  #'Brendan Nyhan'

##	Let's find the types:
follower_dictionary_types = {}
for i in wustl_polsci_followers:
	follower_dictionary_types[i] = "Celebrity" if follower_dictionary_followers[i]>1000 else "Layman"
	follower_dictionary_types[i] = "Expert" if 1000>=follower_dictionary_followers[i]>100 else "Layman"



##	Let's be cautious and save each by followers each ID:
os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020')
follower = {}
with io.open('hw_gencer_3_numbtweets.csv', 'w', encoding="utf-8") as f:	# I used "io.open" bc unicide couldn't  
	w = csv.DictWriter(f, fieldnames = ("ID", "Number_Tweets", "Number_Followers", "Type"))
	w.writeheader()
	for key in follower_dictionary:
		follower["ID"] = key
		follower["Number_Tweets"] = follower_dictionary[key]
		follower["Number_Followers"] = follower_dictionary_followers[key] 
		follower["Type"] = follower_dictionary_types[key]
		w.writerow(follower)


data = pd.read_csv("hw_gencer_3_numbtweets.csv") 
