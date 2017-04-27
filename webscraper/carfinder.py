

import requests
from lxml import html


toyhtml = "https://sfbay.craigslist.org/search/nby/sss?query=toyota&sort=rel&max_price=7000&min_auto_year=2007&auto_title_status=1&auto_transmission=2"

def main():
	toyota = requests.get(toyhtml)

	tree = html.fromstring(toyota.content)
	cars = tree.xpath('//*[@class="result-title hdrlnk"]/text()')
	pricedoubled = tree.xpath('//span[@class="result-price"]/text()')
	#location = tree.xpath('//*[@class="result-hood"]/text()')

	i = 0
	price = []
	for p in pricedoubled:
		if i%2 == 0:
			price.append(p)

		i = i + 1

	print(cars[:10])
	print(price[:10])
	#print(location)

	print(len(cars))
	print(len(price))
	print(len(location))


if __name__ == '__main__':
	main()