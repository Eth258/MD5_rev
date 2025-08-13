'''
首先是get接口  获取各种东西
然后得到照片和滑块
然后是check
'''
import execjs
import requests
import json
import base64
import ddddocr

def b64ToPic(img_data,filename):
    # 假设这是从服务器返回的 Base64 编码的 PNG 图像数据
    base64_string = img_data

    # 解码 Base64 字符串
    image_data = base64.b64decode(base64_string)

    # 将解码后的二进制数据写入到 PNG 文件
    with open(f"{filename}.png", "wb") as image_file:
        image_file.write(image_data)
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
url = "https://neustudy.neumooc.com/web-api/system/captcha/get"
data = {
    "captchaType": "blockPuzzle"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)
# print(response.json())
data=response.json()

img_data_tupian = data.get('repData').get('originalImageBase64')
img_data_huakuai = data.get('repData').get('jigsawImageBase64')


b64ToPic(img_data_tupian , 'originalImage')
b64ToPic(img_data_huakuai , 'jigsawImage')

det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

with open('jigsawImage.png', 'rb') as f:
    target_bytes = f.read()

with open('originalImage.png', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes, simple_target=True)
x=res.get('target')[0]
key=data.get('repData').get('secretKey')
token=data.get('repData').get('token')
check=execjs.compile(open('aes.js','r',encoding='utf-8').read()).call('get_aes_sign',int(x),key)

print(check)
print(res)
print(x)
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
    "pointJson": check,
    "token": token
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)





