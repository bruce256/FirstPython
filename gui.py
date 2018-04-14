#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *  # 导入 Tkinter 库

root = Tk()  # 创建窗口对象的背景色
# 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)
for item in li:  # 第一个小部件插入数据
	listb.insert(0, item)

for item in movie:  # 第二个小部件插入数据
	listb2.insert(0, item)


def buttonListener2(event):  # 创建事件，退出程序
	print("button")
	print(event.x)
	print(event.y)
	# exit()


b1 = Button(root, {"text": "ok", "background": "red"})
b1.bind("<Button-1>", buttonListener2)

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()
b1.pack()
root.mainloop()  # 进入消息循环
