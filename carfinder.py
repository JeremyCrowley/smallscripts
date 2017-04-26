

import requests
from lxml import html


toyhtml = "https://sfbay.craigslist.org/search/nby/sss?query=toyota&sort=rel&max_price=7000&min_auto_year=2007&auto_title_status=1&auto_transmission=2"

def main():
	toyota = requests.get(toyhtml)

	tree = html.fromstring(toyota.content)

	cars = tree.xpath('//a[@class="results-title hdrlnk"]/text()')

	price = tree.xpath('//span[@class="result-price"]/text()')

	print(cars)
	print(price)


if __name__ == '__main__':
	main()