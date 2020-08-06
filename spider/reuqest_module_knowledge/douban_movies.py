# -*- coding:utf-8 -*-
# Author: Nick
import requests
import json
url = "https://movie.douban.com/j/chart/top_list"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
params = {
    "type": "6",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}
response = requests.get(url=url, params=params, headers=headers)

list_data = response.json()
fp = open("./douban.json", "w")
json.dump(obj=list_data, fp=fp, ensure_ascii=False)
print("Successfully")