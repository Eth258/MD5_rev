import time
from hashlib import md5
from urllib import parse
import json

import requests


params = {
    "cityId": "354",
    "cinemaId": "651",
    "day": "0"
}
Ccode='1_3'
uri='/movie/hot_show.api?'+parse.urlencode(params)
timestamp=int(time.time()*1000)
input=f'Wanda{Ccode}FA425A3F9F5FFFC4389994548F83298776F8B46B752A83A6A798C6ED8FE8BFE1{timestamp}'+uri
check=md5(input.encode())
check=check.hexdigest()
print(check)


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
}
# 构造 MX-API 的值：一个 JSON 字符串
mx_api_data = {
    "ver": "7.0.0",
    "sCode": "Wanda",
    "_mi_": "",
    "width": 1280,
    "json": True,
    "cCode": "1_3",
    # "check": "ad1f7dff4a3b92c3906dc589d34c66fe",
    # "ts": 1753788419771,
    "check": check,
    "ts": timestamp,
    "heigth": 720,  # 注意：应该是 "height"，拼写错误可能影响结果
    "appId": "3",
}

# 使用 json.dumps 将字典转为 JSON 字符串
headers["MX-API"] = json.dumps(mx_api_data, ensure_ascii=False)  # ensure_ascii=False 避免中文被转义
url = "https://cinema-api-prd-mx.wandafilm.com/movie/hot_show.api"
# url = "https://cinema-api-prd-mx.wandafilm.com"

response = requests.get(url, headers=headers, params=params)

print(response.text)


