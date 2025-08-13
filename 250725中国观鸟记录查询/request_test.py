import execjs
import requests
import time
import json
from loguru import logger

_timestamp=str(time.time())

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.birdreport.cn",
    "Referer": "https://www.birdreport.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    # "requestId": "76e369bd02d91049800b375004e70604",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    # "sign": "0c4fd3e36986e28280e66c6adf938cbd",
    # "timestamp": 23121
}

header_local = execjs.compile(open('header.js','r',encoding='utf-8').read()).call('get_header',"page=2&limit=20")
headers['requestId']=header_local['requestId']
headers['sign']=header_local['sign']
headers['timestamp']=header_local['timestamp']

url = "https://api.birdreport.cn/front/activity/search"
data = header_local['data']

response = requests.post(url, headers=headers, data=data)

encData=response.json()['data']

decData=execjs.compile(open('header.js','r',encoding='utf-8').read()).call('dec',encData)

decData=json.loads(decData)
print(json.dumps(decData, indent=2, ensure_ascii=False))
