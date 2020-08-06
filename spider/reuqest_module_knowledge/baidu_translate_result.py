# -*- coding:utf-8 -*-
# Author: Nick
import requests
import json

post_url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
word = input("Enter a word: ")
data = {
    "kw": word
}
response = requests.post(url=post_url, data=data, headers=headers)
response_json = response.json()
file_name = word + ".json"
fp = open(file_name, "w")
json.dump(obj=response_json, fp=fp, ensure_ascii=False)
print(f"Successfully get {word} translation")

