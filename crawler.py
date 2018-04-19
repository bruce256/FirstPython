#!/usr/bin/env python
# encoding=utf-8

import requests
from bs4 import BeautifulSoup
from requests import HTTPError

DOWNLOAD_URL = 'http://movie.douban.com/top250'


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
	soup = BeautifulSoup(html)
	movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
	for movie_li in movie_list_soup.find_all('li'):
		detail = movie_li.find('div', attrs={'class': 'hd'})
		a_tag = detail.find('a', attrs={})
		movie_name = detail.find('span', attrs={'class': 'title'}).getText()
		print(movie_name)
		print(a_tag['href'])


def main():
	counter = 0
	while counter < 10:
		start = 25 * counter
		html = download_page(DOWNLOAD_URL + '?start=' + start.__str__())
		parse_html(html)
		counter += 1


if __name__ == '__main__':
	main()
