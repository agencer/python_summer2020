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

https://petitions.whitehouse.gov/petitions?page=2

# Set WD
os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020')


with open('hw_gencer_2.csv', 'w') as f:
	w = csv.DictWriter(f, fieldnames = ("Title", "Published date", "Issues", "Number of signatures"))
	w.writeheader()
	# Open the main website
	for i in range(1,3):
		web_address = 'https://petitions.whitehouse.gov/petitions?page=' + i
		web_page = urllib.request.urlopen(web_address)
		# Parse it
		soup = BeautifulSoup(web_page.read())
		# Find all faculty members
		fac = soup.find_all('article', class_ = 'faculty-post')
		# Loop over fac
		for i in fac:
			prof = {}
			# Name
			prof['name'] = i.h3.text
			# Title
			prof['title'] = i.find('ul').text.lstrip().rstrip()
			# Email
			prof['email'] = i.find(class_ = 'column contact').text.split(': ')[1]
			# Open prof website to get specialization
			try:
				faculty_page = urllib.request.urlopen("https://polisci.wustl.edu" + i.find('a')['href'])
				# webpage
				prof['website'] = "https://polisci.wustl.edu" + i.find('a')['href']
				# Parse it
				soup = BeautifulSoup(faculty_page.read())
			except urllib.error.URLError:
				prof['website'] = i.find('a')['href']
				prof['specialization'] = 'NA'
				continue
			# research interest
			try:
				prof['specialization'] = soup.find(class_ = 'post-excerpt').text
			except AttributeError:
				prof['specialization'] = 'NA'
			w.writerow(prof)



