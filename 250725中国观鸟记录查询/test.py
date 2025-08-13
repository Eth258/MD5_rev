import requests
import json
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://neustudy.neumooc.com",
    "Pragma": "no-cache",
    "Referer": "https://neustudy.neumooc.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://neustudy.neumooc.com/web-api/system/captcha/check"
data = {
    "captchaType": "blockPuzzle",
    "pointJson": "7vsyWOZBtNCzeq04YUHde/O0qGV+DgK3ToqIOhFAbt0=",
    "token": "3f54d9d9a4e54971a6c1a95499198e03"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)