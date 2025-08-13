import requests
from sign1 import first_request
import time
from hashlib import md5
_timestamp=int(time.time()*1000)
key=first_request()
def get_sign(_timestamp,key):
    # data = f"client=fanyideskweb&mysticTime={_timestamp}&product=webfanyi&key=SRz6r3IGA6lj9i5zW0OYqgVZOtLDQe3e"
    data = f"client=fanyideskweb&mysticTime={_timestamp}&product=webfanyi&key={key}"
    sign = md5(data.encode('utf-8')).hexdigest()
    # print(sign)
    return sign

def send():
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://fanyi.youdao.com",
    "Referer": "https://fanyi.youdao.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
    }

    url = "https://dict.youdao.com/webtranslate"
    data = {
    "i": "hi",
    "from": "auto",
    "to": "",
    "keyid": "webfanyi",
    # "sign": "269d808d3ea580ba0c6f8e0b8e445aed",
    "sign": get_sign(_timestamp,key),
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime":  str(_timestamp),

    }
    response = requests.post(url, headers=headers,  data=data)
    return response.text
    # print(response.text)
