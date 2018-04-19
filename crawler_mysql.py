#!/usr/bin/env python
# encoding=utf-8

import requests
from bs4 import BeautifulSoup
import pymysql
from pymysql import Error

DOWNLOAD_URL = 'http://movie.douban.com/top250'
# 打开数据库连接
db = pymysql.connect(host="localhost",
                     user="root",
                     password="",
                     db="test",
                     charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


def download_page(url):
	data = requests.get(url).content
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
		insert(movie_name, a_tag['href'])


def insert(name, url):
	sql = "INSERT INTO dou_ban(name,url) VALUES ('%s', '%s')" % (name, url)
	try:
		# 执行sql语句
		cursor.execute(sql)
		# 提交到数据库执行
		db.commit()
	except Error as err:
		print("Error: unable to insert data", err.__traceback__)
		# 如果发生错误则回滚
		db.rollback()


def main():
	counter = 0
	while counter < 10:
		start = 25 * counter
		html = download_page(DOWNLOAD_URL + '?start=' + start.__str__())
		parse_html(html)
		counter += 1
	# 关闭数据库连接
	db.close()


if __name__ == '__main__':
	main()
