############################################################################################
####								  PYTHON PROJECT									####
####								Alper Sukru Gencer 									####
############################################################################################


##
##
##
## 	Go to https://www.presidency.ucsb.edu/documents/app-categories/written-presidential-orders/presidential/executive-orders
## 	Scraping all presidential executive orders by the President Donald Trump.
## 	Create a .csv file with the following information for each executive oreder:
#	1		Executive Order Title
#	2		Executive Ordder No
#	3		Published date
#	4		Order Text

from bs4 import BeautifulSoup
import urllib
import csv
import os
import io
import re 

# 	Set WD
os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020/Summer_Project/')


def executiveorder_Monster(from_page = 0, to_page):
	with io.open('gencer_exeorder.csv', 'w', encoding="utf-8") as f:	# I used "io.open" bc unicide couldn't  
		w = csv.DictWriter(f, fieldnames = ("OrderTitle", "OrderURL", "OrderNo", "OrderPublishedDate", "OrderText", "OrderText2"))
		w.writeheader()
		# 	Open the main website
		for k in range(from_page,page_number):
			web_address = 'https://www.presidency.ucsb.edu/documents/app-categories/written-presidential-orders/presidential/executive-orders?items_per_page=25&page=' + str(to_page)
			web_page = urllib.request.urlopen(web_address)
			# 	Parse it
			soup = BeautifulSoup(web_page.read())
			# 	Let's create an empty list to put information of each order:
			order_dictionary = {}
			#	Now I want to look at not whole page but individual articles:
			tempo_soup = soup.find_all('p')
			little_soup = []
			for i in range(2, 52,2):
				little_soup.append(tempo_soup[i])
			for l in little_soup:
				#	"OrderTitle"
				info = l.getText().split("—")
				order_dictionary["OrderTitle"] = info[1]
				#	"OrderURL"
				info_url = l.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
				order_dictionary["OrderURL"] = "https://www.presidency.ucsb.edu" + info_url
				#	"OrderNo"
				order_dictionary["OrderNo"] = info[0][-5:]
				#	"OrderPublishedDate"				
				meta_soup = BeautifulSoup((urllib.request.urlopen(order_dictionary["OrderURL"])).read())
				info_date = str(meta_soup.find_all('span', "date-display-single"))
				order_dictionary["OrderPublishedDate"] = re.split("\"", info_date)[3][0:10]
				#	"OrderText"
				tempo_text = []
				info_text = meta_soup.find_all('div', "field-docs-content")
				for i in info_text:
					tempo_text.append(i.getText())
				real_text = ' '.join(tempo_text)
				if len(real_text) >  8192:										#	There is a character restrictiom in excel over 8192 characters.
					real_text2 = real_text[8100:]								#	If text is greater than that, I divide the text into two.
					real_text = real_text[:8100]								
					order_dictionary["OrderText2"] = real_text2
					order_dictionary["OrderText"] = real_text
				else:
					order_dictionary["OrderText"] = real_text
					order_dictionary["OrderText2"] = ""
				w.writerow(order_dictionary)
				print("Presidential Order No", order_dictionary["OrderNo"], " is added to the CSV file.")



##	Let's try:

executiveorder_Monster(10)

##	My code worked:

##	Problems with four orders with different html structure:
#		-	13780
#		-	13842
#		-	13843
#       -	13844
#		-	13846

## 	I realized the problem is about excel's chracter restriction per cell. Some order text has a length greater than 8192.

##	Then I corrected the code. Now I have all orders since 1/20/2017.