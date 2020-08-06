# -*- coding:utf-8 -*-
# Author: Nick
import requests
from pyzipcode import ZipCodeDatabase
import json

url = "https://www.mcdonalds.com/googleapps/GoogleRestaurantLocAction.do"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
my_zipcode = int(input("Enter your zipcode: "))
zcdb = ZipCodeDatabase()
zipcode = zcdb[my_zipcode]
my_latitude = str(zipcode.latitude)
my_longitude = str(zipcode.longitude)

params = {
    "method": "searchLocation",
    "latitude": my_latitude,
    "longitude": my_longitude,
    "radius": "8.045",
    "maxResults": "30",
    "country": "us",
    "language": "en-us",
    "webStatusShowClosed": "false",
    "showClosed": "",
    "hours24Text": "Open 24 hr"
}

response = requests.get(url=url, params=params, headers=headers)
data_json = response.json()
fileName = f"./{my_zipcode}_mcdonalds_restaurant.json"
fp = open(fileName, "w")
json.dump(obj=data_json, fp=fp, ensure_ascii=False)
print("Got all restaurants around me")
