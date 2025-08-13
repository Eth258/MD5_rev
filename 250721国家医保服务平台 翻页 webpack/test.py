import requests
import json


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
    "X-Tingyun": "c=B|4Nl_NnGbjwY;x=6ea08f99e57640da",
    "channel": "web",
    "contentType": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-tif-nonce": "Y6vFXhId",
    "x-tif-paasid": "undefined",
    "x-tif-signature": "2df1ad9112c4d29a15569b78f68f3b7fa2db0c5a8a4361dde6dff2c9ee595655",
    "x-tif-timestamp": "1751986157"
}
cookies = {
    "yb_header_active": "-1",
    "acw_tc": "276aedef17519861579411259e43ba4e860e11eee18b3f31a39bcf2a57e1c4"
}
url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital"
data = {
    "data": {
        "data": {
            "encData": "3DFBCA4667B978F639BB23B95DCE4CC74CE34C33DC32F1068E9E23CA546C9EA8CCD20943B4DAE96380B41164D761DE9742C84A985FE3BABC31CB352556BB87C9C1495DB24A29AB6BC3A85AB7FCA00F33C56677481A67C67F739EE2C7D589054DC373615B5DDB33C24C5B31E61CB7643E8CCAA19EAE1FD36157CF9869E3A3753ED0B4E7BB97C60BF8E5275CAFCAFD1E13E384C10195003FD638576645B5EF45EA"
        },
        "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
        "version": "1.0.0",
        "encType": "SM4",
        "signType": "SM2",
        "timestamp": 1751986157,
        "signData": "hAc2CJ1hQY5D///9GFKMeJndsK7z9K6YZBqaFH46egrAM4vG+u+Ce9276XokSYc1gG4k8d6IoQmQ2ZsWXpvJ8w=="
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)