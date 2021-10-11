#!/usr/bin/python3
# coding=utf-8
import pymysql

# 打开数据库连接
from pymysql import Error

db = pymysql.connect("localhost", "root", "", "test") # charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

sql = "INSERT INTO dou_ban(name,url) VALUES ('%s', '%s')" % ("辩护人", "https://movie.douban.com/subject/21937445/")

try:
	# 执行sql语句
	cursor.execute(sql)
	# 提交到数据库执行
	db.commit()
except Error as err:
	print("Error: unable to insert data", err.__traceback__)
	# 如果发生错误则回滚
	db.rollback()

# SQL 查询语句
sql = "SELECT * FROM dou_ban"
try:
	# 执行SQL语句
	cursor.execute(sql)
	# 获取所有记录列表
	results = cursor.fetchall()
	for row in results:
		id = row[0]
		lname = row[1]
		url = row[2]
		# 打印结果
		print("id=%d,lname=%s, url=%s" % (id, lname, url))
except Error as err:
	print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
