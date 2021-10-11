#!/usr/bin/python3

# 写文件
with open("redis.txt", "wt", encoding="utf-8") as out_file:
    for i in range(1000000):
        out_file.write("set key" + str(i) + " value" + str(i) + "\n")

# Read a file
# with open("test.txt", "rt", encoding="utf-8") as in_file:
# 	text = in_file.read()

# print(text)
