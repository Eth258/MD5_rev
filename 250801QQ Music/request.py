import base64

import execjs
import requests


data='{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topid":5,"offset":0,"num":20,"period":"2025_31"}}}'

sign_data=execjs.compile(open('sign.js','r',encoding='utf-8').read()).call('get_sign',data)
# print(sign_data)
enc_data=execjs.compile(open('data.js','r',encoding='utf-8').read()).call('get_data',data)
# print(enc_data)
headers = {
    "accept": "application/octet-stream",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "text/plain",
    "origin": "https://y.qq.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://y.qq.com/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "pgv_pvid": "9433840555",
    "fqm_pvqid": "6dbe5945-9ca2-4492-9880-0f7300ab3947",
    "fqm_sessionid": "219ad5a4-c83c-44c4-aa62-425d31f02d81",
    "pgv_info": "ssid=s1916798084",
    "ts_uid": "962962266"
}
url = "https://u6.y.qq.com/cgi-bin/musics.fcg"
params = {
    "_": "1754635655663",
    "encoding": "ag-1",
    "sign": sign_data
}
# data1 = 'D2HebdKgsJlLz89UH5wU5AlpS5lBZhrVQZ8oogrefx2I2KIecyvbKK7NI1odRI9ke09MIN3VBYJpdVYx00tY/pvBpExkGTnnrQLzecfiNyt/kYSUHF21zSzoTsjx1l+nrSjoixT5c2Uvve7kL8zqheea7F6C5++j7BnEN3kFgkgbfs9Lud+iQeERnIktTI8SksJKnKcWYhCvOFSDv5rlnOk/b50p30vHhitgtXoXdPT8vuEID6amUxUr5hA8JxNmaWF/u/wP6xU1x19PQZvotMvU5yoqznnoB/ZyPPfH6wh3DRZDEMLp9M8qr8zBrjSevUiRgb6VERxvI/2YqUpK5NOVjZkIhzGhqg6qTO53WqTZ8Q5pQhiDth42HkZt76XAK8HriW4vPazR61dol5jgkYE07z44tOP8von+qrsrw7cVsN9gFoneak7YxKcwrYpkDAVrXpeT'.encode('unicode_escape')
data = enc_data
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
# print(response.text)

b64_data = base64.b64encode(response.content).decode("utf-8")
# print(b64_data)

result = execjs.compile(open("data.js", "r", encoding="utf-8").read()).call("dec_data", b64_data)


print(result)
