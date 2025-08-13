import blackboxprotobuf
import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/grpc-web+proto",
    "cookies": "CASTGC=TGT-3485599-X1yzf6nBOM0jUMOFlW3cMFBNqM6vw30fQVzkLezntK3vRLPHac-auth-iploginservice-79c46fff65-r7zlj;CASTGCSpecial=;",
    "origin": "https://s.wanfangdata.com.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://s.wanfangdata.com.cn/paper?q=%E5%9C%B0%E7%90%83&p=1",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-grpc-web": "1",
    "x-user-agent": "grpc-web-javascript/0.1"
}
cookies = {
    "UM_distinctid": "19830112a1245f-054de382b7800a-26011151-1bcab9-19830112a139d2",
    "CASTGC": "TGT-3485599-X1yzf6nBOM0jUMOFlW3cMFBNqM6vw30fQVzkLezntK3vRLPHac-auth-iploginservice-79c46fff65-r7zlj",
    "WFKS.Auth": "%7B%22Context%22%3A%7B%22AccountIds%22%3A%5B%22Group.dglgxy%22%2C%22trical.WFMinerBalanceLimitRetail%22%2C%22trical.WFTopicBalanceLimitRetail%22%2C%22trical.KxBalanceLimit%22%2C%22GBalanceLimit.dglgxy%22%5D%2C%22Data%22%3A%5B%7B%22Key%22%3A%22Group.dglgxy.DisplayName%22%2C%22Value%22%3A%22%E4%B8%9C%E8%8E%9E%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2%E5%9B%BE%E4%B9%A6%E9%A6%86%22%7D%5D%2C%22SessionId%22%3A%22ddc5a202-f9f6-4cd9-9a74-63ef4b94fa23%22%2C%22Sign%22%3A%22bYoyiNemc2eaylVqtzVAk83IBHAwyZ9GSsxqzuL6Z97E53yQW6ELCQcRPjtbLR%5C%2FR%22%7D%2C%22LastUpdate%22%3A%222025-07-28T08%3A03%3A46Z%22%2C%22TicketSign%22%3A%22%2BS5wzA%2B8zlSUEyyS1KjCFw%3D%3D%22%2C%22UserIp%22%3Anull%7D",
    "zh_choose": "n",
    "Hm_lvt_838fbc4154ad87515435bf1e10023fab": "1753153088,1753689825",
    "HMACCOUNT": "2CE5DA5BE719C704",
    "Hm_lpvt_838fbc4154ad87515435bf1e10023fab": "1753690047",
    "CNZZDATA1281185085": "1515177046-1753690047-https%253A%252F%252Fwww.wanfangdata.com.cn%252F%7C1753690047"
}

hex_string='0a180a0570617065721206e59cb0e790832801301442010048011001'

bytes_string=bytes.fromhex(hex_string)

dec_data,message_type=blackboxprotobuf.protobuf_to_json(bytes_string)

orign_data={
  "1": {
    "1": "paper",
    "2": "爬虫",
    "5": 1,
    "6": 2,
    "8": "\u0000",
    "9": 1
  },
  "2": 1
}

bytes_data=bytes(blackboxprotobuf.encode_message(orign_data,message_type))

url = "https://s.wanfangdata.com.cn/SearchService.SearchService/search"
data =bytes([0,0,0,0,len(bytes_data)])+bytes_data
response = requests.post(url, headers=headers, cookies=cookies, data=data)

response_data,message_type=blackboxprotobuf.protobuf_to_json(response.content[5:])
print(response_data)
# print(len(bytes_data))