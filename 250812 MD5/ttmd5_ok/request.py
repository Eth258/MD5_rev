import requests

def dec_ttmd5(chip):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "http://ttmd5.com/index.php?lang=cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    cookies = {
        # 这里可以根据需要填
    }
    url = "http://ttmd5.com/do.php"
    params = {
        "c": "Decode",
        "m": "getMD5",
        "md5": chip
    }

    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
        response.raise_for_status()
        data = response.json()

        cipher = data.get('cipher', '')
        plain = data.get('plain', '')
        typ = data.get('type', '')
        if typ=='':
            typ='md5'

        print(f"ttmd5: '{{\"{cipher}\": \"{plain}\"}} 类型: {typ}")


        # return data
    except Exception as e:
        print(f"请求失败: {e}")
        return None
