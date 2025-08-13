import requests


def dec_t007(chip):

    try:
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.t007.cn",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.t007.cn/",
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
            # "PHPSESSID": "fcc38k4vbhjnos1vkpo5hhh7e0",
            # "Hm_lvt_c9cde959104b80f94a4f02455eb8e298": "1755014535,1755073873",
            # "Hm_lpvt_c9cde959104b80f94a4f02455eb8e298": "1755073873",
            # "HMACCOUNT": "707E01F1B4331C51",
            # "Hm_lvt_ae5efad7958433957623b3bd74e869b8": "1755014535,1755073873",
            # "Hm_lpvt_ae5efad7958433957623b3bd74e869b8": "1755073873"
        }
        url = "https://www.t007.cn/home/index/doEnDecode"
        data = {
            "type": "1",
            "txtInput": "e10adc3949ba59abbe56e057f20f883e",
            "salt": "",
            "ciphertype_id": "1",
            "rnd": "0.24499924088486869"
        }
        response = requests.post(url, headers=headers, cookies=cookies, data=data)

        print("t007:",response.json())
        # return response.json()
    except requests.RequestException as e:
        print(f"请求异常: {e}")
    except ValueError:
        print("返回内容非JSON格式")
    except Exception as e:
        print(f"未知异常: {e}")
