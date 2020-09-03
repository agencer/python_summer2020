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


# Set WD
os.chdir('C:/Users/alper/OneDrive/Belgeler/GitHub/python_summer2020')


with open('hw_gencer_2.csv', 'w') as f:
	w = csv.DictWriter(f, fieldnames = ("Title", "Published date", "Issues", "Number of signatures"))
	w.writeheader()
	# Open the main website
	for i in range(1,3):
		web_address = 'https://petitions.whitehouse.gov/petitions?page=' + str(i)
		web_page = urllib.request.urlopen(web_address)
		# Parse it
		soup = BeautifulSoup(web_page.read())
		# Let's create an empty list to put each petition's url:
		petitions = []
		# Let's get each url:
		for a in soup.find_all('a', href=True):
		    if a['href'].startswith("/petition/") and len(a['href'])>20:
		    	petitions.append("https://petitions.whitehouse.gov" + a['href'])
		petitions = list(set(petitions))		
		# Now let's go to each webpage and get related information:
		for i in petitions:
			pet_dictionary = {}
			# Title
			prof['Title'] = i.h3.text
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



web_address = 'https://petitions.whitehouse.gov/petitions?page=' + str(1)
web_page = urllib.request.urlopen(web_address)
soup = BeautifulSoup(web_page)
petitions = []
for a in soup.find_all('a', href=True):
    if a['href'].startswith("/petition/") and len(a['href'])>20:
    	petitions.append(a['href'])
petitions = list(set(petitions))

for i in petitions:
	pet_web_page = urllib.request.urlopen(petitions)
	soup = BeautifulSoup(web_page.read())
	# Let's create a petition dictionary:
	pet_dictionary = {}
	# Title:
	pet_dictionary['Title'] = i.h3.text
	# Issues:
	pet_dictionary['Issues'] = i.find(class_ = 'column contact').text.split(': ')[1]
	# "Date":
	pet_dictionary['Date'] = i.find('ul').text.lstrip().rstrip()

	# Number of signatures:
	pet_dictionary['Signatures'] = i.find(class_ = 'column contact').text.split(': ')[1]

	
example = petitions[0]
pet_web_page = urllib.request.urlopen(example)
soup = BeautifulSoup(pet_web_page.read())
print(soup)
# Let's create a petition dictionary:
pet_dictionary = {}
# Title:
pet_dictionary['Title'] = (soup.h1).getText()
# Issues:
pet_dictionary['Issues'] = [i.getText() for i in soup.find_all("h6")][0]
.find_all(class_ = 'field-items')
.text.split(': ')[1]

	# "Date":
	pet_dictionary['Date'] = i.find('ul').text.lstrip().rstrip()
	# Email:
	pet_dictionary['Email'] = i.find(class_ = 'column contact').text.split(': ')[1]
	# Number of signatures:
	pet_dictionary['Signatures'] = i.find(class_ = 'column contact').text.split(': ')[1]