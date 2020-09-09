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
##			-> Amanda Gomez
##		- Among the followers of @WUSTLPoliSci who is the most popular, i.e. has
##			the greatest number of followers?
##			-> Brendan Nyhan
##		 -Among the friends of @WUSTLPoliSci, i.e. the users she is following, who
##			are the most active layman, expert and celebrity?
##			-> 'usman falalu' (layman), "Tim... we're doomed" (expert), and 'The New York Times' (celebrity)
##		- Among the friends of @WUSTLPoliSci who is the most popular?
##			-> Barack Obama
##
##	Two degrees of separation: For the following two questions, limit your search
##		of followers and friends to laymen and experts.
##		- Among the followers of @WUSTLPoliSci and their followers, who is the
##			most active?
##			-> 
##		- Among the friends of @WUSTLPoliSci and their friends, who is the most
##			active?
##			-> 


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
import numpy as np



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

##	Let's find the most active follower:
follower_dictionary = {}
for i in wustl_polsci_followers:
	follower_dictionary[i] =  (api.get_user(i)).statuses_count 

wustl_polsci_mostactive = max(follower_dictionary, key=follower_dictionary.get) # ID
follower_dictionary[max(follower_dictionary, key=follower_dictionary.get)] # Number of Tweets
api.get_user(wustl_polsci_mostactive).name # Amanda Gomez


##	Let's find the most popular follower:
follower_dictionary_followers = {}
for i in wustl_polsci_followers:
	follower_dictionary_followers[i] = (api.get_user(i)).followers_count

wustl_polsci_mostfollower = max(follower_dictionary_followers, key=follower_dictionary_followers.get) # ID
follower_dictionary_followers[max(follower_dictionary_followers, key=follower_dictionary_followers.get)] # Number of Tweets
api.get_user(wustl_polsci_mostfollower).name  #'Brendan Nyhan'

##	Let's find the types of follower:
follower_dictionary_types = {}
for i in wustl_polsci_followers:
	if follower_dictionary_followers[i] > 1000:
		follower_dictionary_types[i] = "Celebrity"
	elif (follower_dictionary_followers[i] > 100) and (1000 >= follower_dictionary_followers[i]):
		follower_dictionary_types[i] = "Expert" 
	else: 
		follower_dictionary_types[i] = "Layman"


##	Let's find the friends:
wustl_polsci_friends = []
for friend in tweepy.Cursor(api.friends, id ="WUSTLPoliSci").items():
	wustl_polsci_friends.append(friend) 
len(wustl_polsci_friends)	# 158

##	Let's find the most active friend:
friends_dictionary = {}
for i in wustl_polsci_friends:
	friends_id = i.id
	friends_statuses_count = i.statuses_count 
	friends_dictionary[friends_id] =  friends_statuses_count

wustl_polsci_mostactive_friend = max(friends_dictionary, key=friends_dictionary.get) # ID
friends_dictionary[max(friends_dictionary, key=friends_dictionary.get)] # Number of Tweets
api.get_user(wustl_polsci_mostactive_friend).name # 'The New York Times'

##	Let's find the most popular friend:
friends_dictionary_followers = {}
for i in wustl_polsci_friends:
	friends_id = i.id
	friends_follower_count = i.followers_count	
	friends_dictionary_followers[friends_id] = friends_follower_count

wustl_polsci_mostfollower_friends = max(friends_dictionary_followers, key=friends_dictionary_followers.get) # ID
friends_dictionary_followers[max(friends_dictionary_followers, key=friends_dictionary_followers.get)] # Number of Tweets
api.get_user(wustl_polsci_mostfollower_friends).name  #  'Barack Obama'

##	Let's find the types of friend:
friends_dictionary_types = {}
for i in wustl_polsci_friends:
	friends_id = i.id
	friends_follower_count = i.followers_count
	if friends_follower_count > 1000:
		friends_dictionary_types[friends_id] = "Celebrity"
	elif (friends_follower_count > 100) and (1000 >= friends_follower_count):
		friends_dictionary_types[friends_id] = "Expert" 
	else: 
		friends_dictionary_types[friends_id] = "Layman"

api.get_user("764260766").name  #  layman
api.get_user("1064533471").name  #  expert
api.get_user("807095").name  #  celebrity




##	Let's be cautious and save each followers by each ID:
os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020')
follower = {}
with io.open('hw_gencer_3_followerslist.csv', 'w', encoding="utf-8") as f:	# I used "io.open" bc unicide couldn't  
	w = csv.DictWriter(f, fieldnames = ("Follower ID", "Number_Tweets", "Number_Followers", "Type"))
	w.writeheader()
	for key in follower_dictionary:
		follower["Follower ID"] = key
		follower["Number_Tweets"] = follower_dictionary[key]
		follower["Number_Followers"] = follower_dictionary_followers[key] 
		follower["Type"] = follower_dictionary_types[key]
		w.writerow(follower)


##	Let's be cautious and save each friends by each ID:
os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020')
friends = {}
with io.open('hw_gencer_3_friendslist.csv', 'w', encoding="utf-8") as f:	# I used "io.open" bc unicide couldn't  
	w = csv.DictWriter(f, fieldnames = ("Friends ID", "Number_Tweets", "Number_Followers", "Type"))
	w.writeheader()
	for key in friends_dictionary:
		friends["Friends ID"] = key
		friends["Number_Tweets"] = friends_dictionary[key]
		friends["Number_Followers"] = friends_dictionary_followers[key] 
		friends["Type"] = friends_dictionary_types[key]
		w.writerow(friends)



data_followers = pd.read_csv("hw_gencer_3_followerslist.csv") 
data_friends = pd.read_csv("hw_gencer_3_friendslist.csv") 


##	Two degrees of separation: For the following two questions, limit your search
##		of followers and friends to laymen and experts.

new_data_followers = data_followers[data_followers.Type != "Celebrity"]
new_data_followers.head(4)
len(new_data_followers["Follower ID"])
new_data_friends = data_friends[data_friends.Type != "Celebrity"]
new_data_friends.head(4)
len(new_data_friends["Friends ID"])


##		- Among the followers of @WUSTLPoliSci and their followers, who is the
##			most active?
##			-> 

twit_count_followers = {}
follower_tempr_dict = {}
for index, row in new_data_followers.iterrows():
	id_tempr = str(row["Follower ID"])
	follower_tempr = (api.get_user(id_tempr)).followers_ids()
	for i in follower_tempr:
		follower_tempr_dict[i] = (api.get_user(i)).statuses_count
	active_tempr = max(follower_tempr_dict, key=follower_tempr_dict.get)
	activename_tempr = api.get_user(active_tempr).name
	activetweet_tempr = follower_tempr_dict[active_tempr]
	twit_count_followers[id_tempr] = ":".join({str(activetweet_tempr), str(activename_tempr)})



##	Two degrees of separation: For the following two questions, limit your search
##		of followers and friends to laymen and experts.
##		- Among the friends of @WUSTLPoliSci and their friends, who is the most
##			active?
##			-> 

twit_count_friends = {}
follower_tempr_dict = {}
for index, row in new_data_friends.iterrows():
	id_tempr = str(row["Friends ID"])
	follower_tempr = (api.get_user(id_tempr)).followers_ids()
	for i in follower_tempr:
		follower_tempr_dict[i] = (api.get_user(i)).statuses_count
	active_tempr = max(follower_tempr_dict, key=follower_tempr_dict.get)
	activename_tempr = api.get_user(active_tempr).name
	activetweet_tempr = follower_tempr_dict[active_tempr]
	twit_count_followers[id_tempr] = ":".join({str(activetweet_tempr), str(activename_tempr)})


