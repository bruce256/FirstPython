# !/usr/bin/python3

import tkinter
import random
# 导入模块
import support

# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

print("你好，世界")

# 第一个注释
if True:
	print("True")
else:
	print("False")


# name = input("按下 enter 键退出，其他任意键显示...\n")
# print(name)

def test():
	counter = 100  # 赋值整型变量
	miles = 1000.0  # 浮点型
	name = "John"  # 字符串

	print(counter)
	print(miles)
	print(name)


tuple1 = ('runoob', 786, 2.23, 'john', 70.2)
print(tuple1)

tinyDict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(tinyDict)
print(tinyDict['name'])

test()

# 打开一个文件
fo = open("/Users/lvsheng/Downloads/李菁雯-北京邮电大学.pdf", "w")
print("文件名: ", fo.name)
print("访问模式 : ", fo.mode)
print("是否已关闭 : ", fo.closed)
fo.close()
print("是否已关闭 : ", fo.closed)

fo = open("a.txt", "r")
lines = fo.readlines()
print("所有数据", lines)

print(random.randint(1, 100))

list1 = [1, 3, 2]
list1.sort()
print(list1)

# top = tkinter.Tk()
# 进入消息循环
# top.mainloop()
