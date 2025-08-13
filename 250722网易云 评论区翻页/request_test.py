import execjs
import requests
import json

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "nm-gcore-status": "1",
    "origin": "https://music.163.com",
    "priority": "u=1, i",
    "referer": "https://music.163.com/album?id=274252578",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "JSESSIONID-WYYY": "FteGAHNKkEjmZ09ohN%2By1tO5CdB2V%5CvjdDAn3GITZNP9Nu4Muc2lwd4K%5CSdEiGnhnBGY%2FEOxZ%2B78mn5wicqRNNhJ4x%2FC%2B9kpjz6f0kSIqaWUODIO4hV%5Ck9TGJ%2BZ4ndG1qkffgYCJDTOxwj1uP4moXXsg83oo%5CfYpr%2B0B%2BKcS746Kr4tv%3A1752073982537",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "d5fc7bbd24ef3bc6bff1fb175324c7ab,1752072182557",
    "_ntes_nuid": "d5fc7bbd24ef3bc6bff1fb175324c7ab",
    "NMTID": "00O2H2HpWWTxtm3BUt3nEFsPnIoQVYAAAGX76Pf4g",
    "WEVNSM": "1.0.0",
    "WNMCID": "kvegec.1752072183411.01.0",
    "WM_NI": "EGvGhBpJ1DzTo6oQRtl93%2B7DEj5W26WtDmJHq%2BTBFBpvMgY9362jwANWZm005n6Biqm9wdyjFIIU3arQe2wgZ2PODjfjpWZ4H%2B8BcvtwqM%2BYDeL1yKr2QCIcyYuKkHShOUQ%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6ee9be17ea79fbed7bc68babc8eb3c45b968e9aacd66ae9a7bb9ac821ad909f8bcd2af0fea7c3b92a8799baa8eb4ab496ffa5f960adeaa1b2d180b0e7fdccb65087b6fbb8b13e95ac8c8ec944b3f59ca3c54ab4aa8388dc33f1eafe8bf64b8e89968eb33cf7b2faa3ec7bafe7b985fc62869787b6b26bb28fabd3f66d9aeea0b0c762a6b6c0b8d9408cf5f8a3e27eb8a9bfaeaa5388bb84d2fc41b2ee9fa4cc69bb87bbacea4491b881b6d437e2a3",
    "WM_TID": "lhrWVbWmEERFEUAEVUKXb7muzAu5bU3N",
    "__snaker__id": "eqnTyxvXQHYM5mwu",
    "sDeviceId": "YD-CZihQyq2IdtAUgBAEFOSOq2q2U6oO4r0",
    "gdxidpyhxdE": "oKDGGIPOJNe%5CWByzCZ0tZRoDsTBleerWi6RiTvHdq3BJOvoQQXHhqS6CC%2FpRZY6h%5CgJ3VkQGEUHY3hD5J44OwziNYVc%2BPYetdjkZHsqwGR6PE8JsV0epXURUIZz0UHV3i3OOweUq1%2BC47oKGMS%2FhmM7o%5CpbZtE1Ni3KRoHLx1gLpVqa9%3A1752073086513",
    "__remember_me": "true",
    "ntes_utid": "tid._.0T%252FGdl76J3xAA1RBEVfTK%252F3vzEv9Kpve._.0",
    "NTES_YD_SESS": "tnBF6k31EvRORt2GJMQ3W40Mj5FqyKP81aR3Qgd1ZZE8uWdmu57zsx8qpc9i7DCr3HoxgNcVZrrJBui58Rj9wjnIKAp2LPFbyNdFkgBsEu44VZ2iXaXnLndQ5t9SybylIt7m9BpoZs9TemQpPrfYuJzWF77utqCbtDgWxuparNTlQtkyGe_RF3y1nx9H4gi_F9.mWRnIMJW74WJipXH2MKTksTPAjuRYGj3rTYWCCGsPb",
    "S_INFO": "1752072269|0|0&60##|13825551517",
    "P_INFO": "13825551517|1752072269|1|music|00&99|null&null&null#gud&441900#10#0|&0||13825551517",
    "__csrf": "7f7012c9c6e40edae68dc67f82724d73",
    "MUSIC_U": "00896AC928BA54233628350E0DB3C8065DD95CA2FFD1978E543C53B3103F65861441D6D903468A460925D52C9621C0F3E48D9E1AF3D769EF3628637D3A90B7D5B73290C113A9360378D7D0A4F50971BC5A57BB2DAC163B1668E5E38AEB980912359DA126578CE41EAC01945B3AD610A0F80D8A1EE578D6FF7C2F89666CB6ECF80F1D8FB1B99787C59C2B02DB48D4789C63C661F3A40D382D983BD3503F818BE718EBC717779DA227720435C45A7CAC002EFFE914525F55FCB08569AF1FF7398135A2B084A160496D82322692C62D1C301159BF228C12C0440AA8F4EB69EEEB18160F2251AFC5A1956F3B3C1911457F967ACD750456CC68A7AB8A1D42A6CA8CE57DD63359FA7BC00E6453330616DC03905A5CFBBA63B6D0E6E9C76D2405DE34B0E5E12DB167719677056E4F076F850E5D8F09003A9CD98FEFA8035F0897C0D7EC307A38580BADD16A2AA42BEC5C4DE5F9480A9B1058614A35F9BD524B17AE1A5159",
    "ntes_kaola_ad": "1"
}
url = "https://music.163.com/weapi/comment/resource/comments/get"
params = {
    "csrf_token": "7f7012c9c6e40edae68dc67f82724d73"
}
data = {
    "params": "ubMNXO56WD8hPBSG3uAJsjmV99y/t0stQM97vicked9nBgImL68CNFpqec15LDOn4d3w6JuQ5fPMzGsH0HU3/iZdZq9SkqeR41ZP5OavzKBTxtr01zUHH+cQRAzdxveoIGmfi1VqAR+M4HjkR6kaQtlspzAIYWRf7BwDHZ5DcqcQiR0WSA+4tgHEQPyAFkgRSjuTupIia3sEtVWGCUYWAjY8x5TFUtsx6XpmrdBUdY7HoqEEYg2w7wYAsudssAXyLCXpNBfFeAqYs0ienRM8VlmrUViNqT//InrHujRSPYfCEn432Eix+yJoKrM3qSw3mDKuh7qK2bqtRd+xyAGYnfuUOMZmlYj6uV8ELdD4dWY=",
    "encSecKey": "7a55c97f6ac51a6b458bd4329ca6723643c5a56a452b10ac6140ce81c68a159330f21f45b3f22d08d86cd7087a6ec47069795f9b1c6aebc98ba60cc7ccffbfa0b5f3f37795fa9c075b275f0bf115428586c3047f3e49f1917774a4c4f663c1840bb0855862c9ad1dc359e235f2ddb322751f932f5debd3f9c400d1f61014fc47"
}



resqData=execjs.compile(open('encJs.js','r',encoding='utf-8').read()).call('get_params',2122615077,1)

response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(json.dumps(response.json(), indent=2, ensure_ascii=False))
