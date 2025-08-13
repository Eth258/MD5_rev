import requests


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.somd5.com",
    "priority": "u=1, i",
    "referer": "https://www.somd5.com/",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "Hm_lvt_7cbb4bb91b6ffb8d7caebd60d7652ff4": "1754997750",
    "Hm_lpvt_7cbb4bb91b6ffb8d7caebd60d7652ff4": "1754997750",
    "HMACCOUNT": "08170C6F82F2A602",
    "PHPSESSID": "kfiked84qub1scpd1pqrpf38vu"
}
url = "https://www.somd5.com/search.php"
data = {
    "hash": "e10adc3949ba59abbe56e057f20f883e",
    "t": "0",
    "captcha": "t03ieBUzlIptvjUAJnD_rpPeYMBbpO1NH4PtvfCWVTCTwXOf5aJmOMjzA_oT9lSBC86HEJUUHyr8rVdvbXkOQgpg6diUhLkZ9kT7AwHXBos6J8__TzLyO5Eng**|@NEN"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)