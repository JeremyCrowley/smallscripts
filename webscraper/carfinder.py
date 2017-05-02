
import sys

# web scraping
import requests
from lxml import html
import bs4

# for email
import smtplib
from email.mime.text import MIMEText


def main():

	if(len(sys.argv) != 6):
		print("Incorrect input arguments")
		sys.exit()

	# order of input args is as follows
	search = sys.argv[1]	
	minyear = sys.argv[2]
	maxprice = sys.argv[3]
	minprice = sys.argv[4]
	term = sys.argv[5]



	# construct link and get the html
	link = "https://sfbay.craigslist.org/search/nby/sss?sort=date&auto_title_status=1&auto_transmission=2&min_price=" + str(minprice) + "&max_price=" + str(maxprice) + "&min_auto_year=" + str(minyear) + "&query=" + str(search)
	handle = requests.get(link)


	# find the hyper link of the postings
	hyperlink = []
	soup = bs4.BeautifulSoup(handle.content, "lxml")
	for link in soup.findAll("a"):
		if(".html" in link.get("href")):
			if(link.get("href") not in hyperlink):
				hyperlink.append(link.get("href"))


	# get the titles and prices from the postings
	tree = html.fromstring(handle.content)
	cars = tree.xpath('//*[@class="result-title hdrlnk"]/text()')
	price = tree.xpath('//span[@class="result-meta"]//span[@class="result-price"]/text()')
	

	# print out each listing with the given term in the title
	for i in range(0,len(price)):
		if(str(term) in cars[i].encode('utf-8').lower()):
	 		print(cars[i].encode('utf-8') + " --> " + price[i].encode('utf-8'))
	

if __name__ == '__main__':
	main()