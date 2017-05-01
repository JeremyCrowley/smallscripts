

import requests
from lxml import html
import bs4

import smtplib
from email.mime.text import MIMEText



#def message(title, price, url):






def main():

	toyhtml = "https://sfbay.craigslist.org/search/nby/sss?sort=date&auto_title_status=1&auto_transmission=2&max_price=7000&min_auto_year=2007&query=toyota"

	toyota = requests.get(toyhtml)

	hyperlink = []
	
	soup = bs4.BeautifulSoup(toyota.content, "lxml")
	for link in soup.findAll("a"):
		if(".html" in link.get("href")):
			if(link.get("href") not in hyperlink):
				hyperlink.append(link.get("href"))

	tree = html.fromstring(toyota.content)

	cars = tree.xpath('//*[@class="result-title hdrlnk"]/text()')
	price = tree.xpath('//span[@class="result-meta"]//span[@class="result-price"]/text()')
	
	for i in range(0,len(price)):

		if("camry" in cars[i].encode('utf-8').lower() and int(price[i].encode('utf-8')[1:]) < 7000):
			print(cars[i].encode('utf-8') + " --> " + price[i].encode('utf-8'))
	

	

if __name__ == '__main__':
	main()