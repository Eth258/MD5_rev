import json

import requests
import base64

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
cookies = {
    # "Hm_lvt_558277c2aafa11d5d6a6560f1c025aff": "1755001760",
    # "HMACCOUNT": "0B0DB06CE0A7EC2E",
    # "Hm_lpvt_558277c2aafa11d5d6a6560f1c025aff": "1755001796",
    # "koa.sess.pmd5api": "eyJjYXBjaGEiOiI0aFFIIiwiX2V4cGlyZSI6MTc1NTAwMjgzMzg2NSwiX21heEFnZSI6MTIwMDAwfQ==",
    # "koa.sess.pmd5api.sig": "GKp6AUOblxH8FbNTfPHVF03ZOxI"
}


def get_cookie():
    url = "https://api.pmd5.com/pmd5api/checkcode"
    response = requests.get(url, headers=headers, cookies=cookies)
    headers_api=response.headers.get('Set-Cookie').split(';')[0]
    headers_sig=response.headers.get('Set-Cookie').split(';')[3].split(',')[1].strip()
    # print(headers_api)
    # print(headers_sig)
    key, api_value = headers_api.split('=', 1)
    # print(api_value)
    key, sign_value = headers_sig.split('=', 1)
    # print(sign_value)
    checkcode=base64.b64decode(api_value)
    capcha_value = json.loads(checkcode.decode())['capcha']
    # print(capcha_value)
    # with open("download.bmp", "wb") as f:
    #     f.write(response.content)
    return api_value,sign_value,capcha_value



# get_cookie()