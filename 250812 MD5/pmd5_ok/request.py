import requests
from .checkcode import get_cookie


def dec_pmd5(chip):
    # chip="e10adc3949ba59abbe56e057f20f883e"
    try:
        headers_api,headers_sig,capcha_value=get_cookie()

        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "origin": "https://pmd5.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://pmd5.com/",
            "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }
        cookies = {

            "koa.sess.pmd5api": headers_api,
            "koa.sess.pmd5api.sig": headers_sig
        }
        url = "https://api.pmd5.com/pmd5api/pmd5"
        params = {
            "checkcode": capcha_value,
            "pwd": chip
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)

        print('pmd5:',response.json()['result'])
        # pmd5: {'e10adc3949ba59abbe56e057f20f883e': '123456'}
    except requests.RequestException as e:
        print(f"请求异常: {e}")
    except ValueError:
        print("返回内容非JSON格式")
    except Exception as e:
        print(f"未知异常: {e}")

