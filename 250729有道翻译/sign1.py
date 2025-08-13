import requests
from hashlib import md5
import time
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
_timestamp=int(time.time()*1000)
def get_sign(_timestamp):
    data = f"client=fanyideskweb&mysticTime={_timestamp}&product=webfanyi&key=yU5nT5dK3eZ1pI4j"
    sign = md5(data.encode('utf-8')).hexdigest()
    # print(sign)
    return sign

def first_request():
    url = "https://dict.youdao.com/webtranslate/key"
    params = {
        "keyid": "webfanyi-key-getter-2025",
        "sign": get_sign(_timestamp),
        "client": "fanyideskweb",
        "product": "webfanyi",

        "pointParam": "client,mysticTime,product",
        "mysticTime": str(_timestamp),
    }
    response = requests.get(url, headers=headers,  params=params)

    # print(response.json()['data']['secretKey'])
    return response.json()['data']['secretKey']







