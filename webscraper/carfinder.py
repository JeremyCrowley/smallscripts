

import requests
from lxml import html
from email.mime.text import MIMEText
import smtplib


toyhtml = "https://sfbay.craigslist.org/search/nby/sss?sort=date&auto_title_status=1&auto_transmission=2&max_price=7000&min_auto_year=2007&query=toyota"

def main():

	toyota = requests.get(toyhtml)
	tree = html.fromstring(toyota.content)

	cars = tree.xpath('//*[@class="result-title hdrlnk"]/text()')
	price = tree.xpath('//span[@class="result-meta"]//span[@class="result-price"]/text()')
	
	#link = tree.xpath('//*[contains(/text(),"/nby/ctd")]')

	#print link




	for i in range(0,len(price)):

		if("camry" in cars[i].encode('utf-8').lower() and int(price[i].encode('utf-8')[1:]) < 6000):
			print(cars[i].encode('utf-8') + " --> " + price[i].encode('utf-8'))


	

if __name__ == '__main__':
	main()