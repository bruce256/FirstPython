#!/usr/bin/python3

# 写文件
with open("test.txt", "wt", encoding="utf-8") as out_file:
	out_file.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt", "rt", encoding="utf-8") as in_file:
	text = in_file.read()

print(text)
