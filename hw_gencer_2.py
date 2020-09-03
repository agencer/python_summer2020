############################################################################################
####									HOMEWORK										####
####								Alper Sukru Gencer 									####
############################################################################################
##
## 	Go to https://petitions.whitehouse.gov/petitions
## 	Go to the petition page for each of the petitions in the first two pages.
## 	Create a .csv file with the following information for each petition:
#	1		Title
#	2		Published date
#	3		Issues
#	4		Number of signatures

from bs4 import BeautifulSoup
import urllib
import csv
import os
import io

# 	Set WD
os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020')


def petition_monster(page_number):
	with io.open('hw_gencer_2.csv', 'w', encoding="utf-8") as f:	# I used "io.open" bc unicide couldn't  
		w = csv.DictWriter(f, fieldnames = ("Title", "URL", "Number of signatures", "Over 100k signitures", "Issues", "Creator", "Published date"))
		w.writeheader()
		# 	Open the main website
		for k in range(0,page_number):
			web_address = 'https://petitions.whitehouse.gov/?page=' + str(k)
			web_page = urllib.request.urlopen(web_address)
			# 	Parse it
			soup = BeautifulSoup(web_page.read())
			# 	Let's create an empty list to put each petition's url:
			petition_dictionary = {}
			#	Now I want to look at not whole page but individual articles:
			little_soup = soup.find_all('article')
			del little_soup[0]
			for l in range(0,20):
				#	"Title"
				tag_a = little_soup[l].find_all('a', href=True)
				petition_dictionary["Title"] = tag_a[0].getText()
				#	"URL"
				petition_dictionary["URL"] = "https://petitions.whitehouse.gov" + tag_a[0].get("href")
				#	"Number of signatures"
				tag_span = little_soup[l].find_all('span')
				petition_dictionary["Number of signatures"] = tag_span[1].getText ("signatures-number")
				#	"Over 100k signitures"
				petition_dictionary["Over 100k signitures"] = str(int((petition_dictionary["Number of signatures"]).replace(',', '')) >= 100000)
				#	"Issues"
				tag_h6 = little_soup[l].find_all('h6')
				h6_list = []
				for i in range(0,len(tag_h6)):
					h6_list.append(tag_h6[i].getText())	
				petition_dictionary["Issues"] = ", ".join(h6_list)
				#	"Creator" and "Published date"
				meta_soup = BeautifulSoup((urllib.request.urlopen(petition_dictionary["URL"])).read())
				tag_h4 = meta_soup.find_all('h4')[0]
				petition_dictionary["Creator"] = (tag_h4.getText()).split(" on ")[0][len("Created by "):] 
				petition_dictionary["Published date"] = (tag_h4.getText()).split(" on ")[1] 
				w.writerow(petition_dictionary)




#	For the HW I print the first 3 pages (3*20 = 60 items). Therefore,

petition_monster(3) #### YESSS! It has 60 items!!