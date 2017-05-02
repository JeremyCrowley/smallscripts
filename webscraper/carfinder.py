
import sys
import requests
from lxml import html
import bs4
import smtplib
from email.mime.text import MIMEText



def main():

	for arg in sys.argv:
		if arg.isdigit():
			if int(arg) < 2020:
				minyear = arg
			else:
				maxprice = arg
		else:
			search = arg

	link = "https://sfbay.craigslist.org/search/nby/sss?sort=date&auto_title_status=1&auto_transmission=2&max_price=" + str(maxprice) + "&min_auto_year=" + str(minyear) + "&query=" + str(search)
	
	handle = requests.get(link)

	hyperlink = []
	
	soup = bs4.BeautifulSoup(handle.content, "lxml")
	for link in soup.findAll("a"):
		if(".html" in link.get("href")):
			if(link.get("href") not in hyperlink):
				hyperlink.append(link.get("href"))

	tree = html.fromstring(handle.content)

	cars = tree.xpath('//*[@class="result-title hdrlnk"]/text()')
	price = tree.xpath('//span[@class="result-meta"]//span[@class="result-price"]/text()')
	
	for i in range(0,len(price)):

	 	print(cars[i].encode('utf-8') + " --> " + price[i].encode('utf-8'))
	

	

if __name__ == '__main__':
	main()