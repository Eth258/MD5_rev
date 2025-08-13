import json
import requests

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
}

# 构造 MX-API 的值：一个 JSON 字符串
mx_api_data = {
    "ver": "7.0.0",
    "sCode": "Wanda",
    "_mi_": "",
    "width": 1280,
    "json": True,
    "cCode": "1_3",
    "check": "ad1f7dff4a3b92c3906dc589d34c66fe",
    "ts": 1753788419771,
    "heigth": 720,  # 注意：应该是 "height"，拼写错误可能影响结果
    "appId": "3",
}

# 使用 json.dumps 将字典转为 JSON 字符串
headers["MX-API"] = json.dumps(mx_api_data, ensure_ascii=False)  # ensure_ascii=False 避免中文被转义

url = "https://cinema-api-prd-mx.wandafilm.com/movie/hot_show.api"
params = {
    "cityId": "151",
    "cinemaId": "6988",
    "day": "0"
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.text)