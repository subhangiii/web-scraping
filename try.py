#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://news.google.com/search?q=nri&hl=en-IN&gl=IN&ceid=IN%3Aen"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes=[]

table = soup.find('div', attrs = {'class':'lBwEZb BL5WZb xP6mwf'})

for a in table.findAll('div', attrs = {'class':'NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc'}):
    quote = {}
    quote['url'] = a.a['href']
    quotes.append(quote)
filename = 'news.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['url'])
	w.writeheader()
	for quote in quotes:
		w.writerow(quote)
