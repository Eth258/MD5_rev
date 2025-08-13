import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Access-Token": "undefined",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://world.xiaomawang.com",
    "Referer": "https://world.xiaomawang.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://community-api.xiaomawang.com/api/v1/user/comment"
data = {
    "adBizId": None,
    "adType": 0,
    "content": "可以",
    "targetId": "p4db666J",
    "targetType": 1,
    "timestamp": 1754917106,
    "type": 1,
    "uuid": "70a696cf59b540fd",
    "sign": "4bc04fbdd3ed1b664563f8b619769574768e93e676366eb9cbdfc1b3fedbe6fd1aed5c1a77976b1593245ee4c54019e851d2679f5aa725a14373d0b94f14a756"
}

data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)