from urllib import request
from http import cookiejar


url = "http://www.baidu.com"

print('第一种方法')
response1 = request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('第二种方法')
request2 = request.Request(url)
request2.add_header("user-agent", "Mozilla/5.0")
response2 = request.urlopen(request2)
print(response2.getcode())
print(len(response2.read()))

print('第三种方法')
cj = cookiejar.CookieJar()
cookie_support = request.HTTPCookieProcessor(cj)
request.install_opener(request.build_opener(cookie_support))
response2 = request.urlopen(url)
print(response2.getcode())
print(cj)
print(response2.read())