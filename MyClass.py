# !/usr/bin/python3


class MyClass:
	"""一个简单的类实例"""
	i = 12345
	r = 0

	# 构造函数
	def __init__(self, realPart, imagPart):
		self.r = realPart
		self.i = imagPart

	def f(self):
		return 'hello world'

	def hello(self, name):
		self.prt()
		return "hello " + name

	def prt(self):
		print(self)
		print(self.__class__)


# 实例化类
x = MyClass(1, 2)

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i, x.r)
print("MyClass 类的方法 f 输出为：", x.f())
print("MyClass 类的方法 f 输出为：", x.hello("ruzun"))
x.prt()
