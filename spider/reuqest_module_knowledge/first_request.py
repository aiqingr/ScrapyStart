# -*- coding:utf-8 -*-
# Author: Nick
# 1. 指定url
# 2. 发起请求
# 3. 获取相应数据
# 4. 持久化存储
import requests
# 1. 指定url
url = "https://www.sogou.com/"
# 2. 发起请求
response = requests.get(url)
# 3. 获取相应数据
response_text = response.text
print(response_text)
# 4. 持久化存储
with open("./first_request.html", "w") as fp:
    fp.write(response_text)
print("Spider complete!")
