import requests
import urllib

resp = requests.get('https://www.baidu.com')

print(resp.status_code)
print(resp.content)
print("cookies", resp.cookies.__len__())
for i in resp.cookies:
	print(i)
print(resp.elapsed)

response = urllib.request.urlopen('http://movie.douban.com/top250')
print(response.read())
