#!/usr/bin/env python
# encoding=utf-8

import requests
from bs4 import BeautifulSoup
from requests import HTTPError

HTTP_ = 'http:'


def download_page(url):
	print(url)
	try:
		data = requests.get(url).content
	except HTTPError as err:
		print(err.__traceback__)
	except ConnectionError as err:
		print(err.__traceback__)
	except TimeoutError as err:
		print(err.__traceback__)

	return data


def parse_html(html):
	soup = BeautifulSoup(html, "html.parser")
	book_list_soup = soup.find_all('div', attrs={'class': 'p-detail'})
	for book_div in book_list_soup:
		a_tag = book_div.find('a', attrs={'class': 'p-name'})
		print('书名 ： ' + a_tag['title'] + '\t链接 ： ' + HTTP_ + a_tag['href'])
	next_button = soup.find('a', attrs={'class': 'pn-next'})
	return next_button['href']


def main():
	download_url = '//book.jd.com/booktop/0-0-0.html?category=3287-0-0-0-5-1#comfort'
	while download_url != 'javascript:void(0);':
		html = download_page(HTTP_ + download_url)
		download_url = parse_html(html)


if __name__ == '__main__':
	main()
