import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.aqistudy.cn",
    "Referer": "https://www.aqistudy.cn/historydata/daydata.php?city=%E6%B7%B1%E5%9C%B3&month=2014-01",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "Hm_lvt_6088e7f72f5a363447d4bafe03026db8": "1753102790,1753103098",
    "HMACCOUNT": "2CE5DA5BE719C704",
    "Hm_lpvt_6088e7f72f5a363447d4bafe03026db8": "1753103326"
}
url = "https://www.aqistudy.cn/historydata/api/historyapi.php"
data = {
    "hA4Nse2cT": "scJVWVKosHY3PE5vWZ4GunKxt5HeJVNnTTLuWpHjEtos5BH8DMW5qtJ+CBSRim1rRY1A89IPLpgdkWOIUYLNUtDpiB465gmsy2iLtd3DgFSfb8Aj65pM6UyA/zPDZYdTDSpZcW8uORUVobadlRWig4BrEW4/Bw0R0U7P034wvMQ2aTba/QFYhO5ezW+WLsV6N5p05ls8y4lFQqVBDveZnlUHaI+JvkAJiuRN1RCPdKprb3+GvHbMSHe+Yv9/EMGfcfrO9o1Aylnc6C8EYPSE9oDVJRzBbbUDfoRLv9Ir8w272LQR/0Z6wsMbXequsyrzoYWQ/ucKsnksaS/G4x6kzYs6u5FLXdef5gggXpF7faE="
}
requests.packages.urllib3.disable_warnings()
response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)

print(response.text)
print(response)