# -*- coding:utf-8 -*-
# Author: Nick

# UA: User-Agent 请求载体的身份标示
# UA检测：门户网站的服务器会检测相对应的载体身份标示 如果检测到请求的载体身份标示为某一款浏览器
# 说明该请求是一个正常的请求 但是 如果检测到请求的载体身份标示不是基于某一款浏览器的 则表示该请求
# 不是正常的请求（爬虫） 则服务器就有可能拒绝该请求
# UA伪装： 让爬虫请求的身体载体标示伪装成某一款浏览器
import requests
url = "https://www.sogou.com/web"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
parameter_first = input("enter a word: ")
param = {
    "query": parameter_first
}
response = requests.get(url=url, params=param, headers=headers)
page_text = response.text
file_name = parameter_first + ".html"
with open(file_name, "w") as fp:
    fp.write(page_text)
print(f"{file_name} saved!!!!!")