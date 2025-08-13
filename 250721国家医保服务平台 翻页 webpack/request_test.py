import time

import requests
import json
import execjs
_timestamp = int(time.time())

header_params = execjs.compile(open('headerJs.js', 'r', encoding='utf-8').read()).call('header_params')

headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fuwu.nhsa.gov.cn",
    "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    # "X-Tingyun": "c=B|4Nl_NnGbjwY;x=40e2255965f54428",
    "channel": "web",
    "contentType": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    # 其实这几个不用都可以
    # "x-tif-nonce": "s3hYGfim",
    "x-tif-paasid": "undefined",
    # "x-tif-signature": "1c0f3a74f8393c26b7e90b83f2d72a5c1ef0148483323aad5eb58048a09c01b2",
    # "x-tif-timestamp": "1751640832"
}

headers['X-Tingyun'] = header_params['X-Tingyun']
headers['x-tif-nonce'] = header_params['x-tif-nonce']
headers['x-tif-signature'] = header_params['x-tif-signature']
headers['x-tif-timestamp'] = str(header_params['x-tif-timestamp'])

cookies = {
    "yb_header_active": "-1",
    "acw_tc": "276aedef17519861579411259e43ba4e860e11eee18b3f31a39bcf2a57e1c4"
}
url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital"

data1={
    "data": {
        "addr": "",
        "regnCode": "441900",
        "medinsName": "",
        "medinsLvCode": "",
        "medinsTypeCode": "",
        "outMedOpenFlag": "",
        "pageNum": 2,
        "pageSize": 10,
        "queryDataSource": "es"
    },
    "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
    "version": "1.0.0",
    "encType": "SM4",
    "signType": "SM2",
    "timestamp": 1751987845
}
signData = execjs.compile(open('base_func.js', 'r', encoding='utf-8').read()).call('get_signData',data1)
data2={
    "data": {
        "addr": "",
        "regnCode": "441900",
        "medinsName": "",
        "medinsLvCode": "",
        "medinsTypeCode": "",
        "outMedOpenFlag": "",
        "pageNum": 2,
        "pageSize": 10,
        "queryDataSource": "es"
    },
    "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
    "version": "1.0.0",
    "encType": "SM4",
    "signType": "SM2",
    "timestamp": 1751987845,
    "signData": "HGMtWVrhJrN6VJwClWPI2imsR9QiUZFnmNJTIIY0UVbOtPYTxEMom6RHViGl8zNgsOiSHlrylgU7OLMFQE0Iow"
}

encData = execjs.compile(open('base_func.js', 'r', encoding='utf-8').read()).call('get_enc_data',data2)

data = {
    "data": {
        "data": {
            "encData": encData
        },
        "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
        "version": "1.0.0",
        "encType": "SM4",
        "signType": "SM2",
        "timestamp": 1751987845,
        "signData": "HGMtWVrhJrN6VJwClWPI2imsR9QiUZFnmNJTIIY0UVbOtPYTxEMom6RHViGl8zNgsOiSHlrylgU7OLMFQE0Iow"
    }
}


data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)
