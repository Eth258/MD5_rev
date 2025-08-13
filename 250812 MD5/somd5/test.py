import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://t.captcha.qq.com",
    "Referer": "https://t.captcha.qq.com/cap_union_new_show?aid=2096770183&protocol=https&accver=1&showtype=popup&ua=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMi4wLjAuMCBTYWZhcmkvNTM3LjM2&noheader=1&fb=1&aged=0&enableAged=0&enableDarkMode=0&grayscale=1&dyeid=0&clientype=2&sess=s0znbGv_sZes8ZFhQTet3mf5YKhzuY4tipTfOV7bGAA_ONIeqn0kFyFd3mBM0_ct_H1XtWvV7QCOPxaQkDVpF-XsK7oXuHDpD8D7KAJlJEBr43dmyE--Ylf5I-Cx_UJ-dHehfiYH2N2Awvrg-RYNqBqakQvJRDvUG6zL--cm0aL2yPuGHsCoV2-y6MG7_CF0wMDfimrDqcA3MFBlkkvq0ZQn55Wui5fGg-zJ7ym1zXNyM-SjgDYrLhBsvxYTvszUDaBs1RYm2iGhmsNVh8ChpU7A**&fwidth=0&sid=7361003269489754112&wxLang=&tcScale=1&uid=&cap_cd=&rnd=185834&prehandleLoadTime=110&createIframeStart=1754999938506&global=0&subsid=6",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://t.captcha.qq.com/cap_union_new_verify"
data = {
    "aid": "2096770183",
    "protocol": "https",
    "accver": "1",
    "showtype": "popup",
    "ua": "TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMi4wLjAuMCBTYWZhcmkvNTM3LjM2",
    "noheader": "1",
    "fb": "1",
    "aged": "0",
    "enableAged": "0",
    "enableDarkMode": "0",
    "grayscale": "1",
    "dyeid": "0",
    "clientype": "2",
    "sess": "s0Ux7hTn26AgnbOjQzE0YMO37ht49eBbe-p7ZH1FCZlbIi27haWqXNtJvqHS4OSBVFud2mkxRDQEkoOYGDCv_CAKAB211RMWKkyMotDKGGR4bbcizJKR83SmhwJF5O_CNlSki4K-BHQF6j8iBH3psNAywNLoDwWwZMyRFqrHxncRJPP5OdkFMfck2ck69WAhDP3Jao1m3G_K1CsHVs3y4rPd3RXoP1T3wprS83EY_m5sLns3Tb8XDfjEASHKhrYRpn8pm80aZ1RlDI3MYwNxZ1jfL0dsT8drQtlpEL-v3aeW5_MFzmR7UvmTYWANDbVdtf9fN56eeYAeSbUuVxdC6Mpw**",
    "fwidth": "0",
    "sid": "7361003269489754112",
    "wxLang": "",
    "tcScale": "1",
    "uid": "",
    "cap_cd": "",
    "rnd": "185834",
    "prehandleLoadTime": "110",
    "createIframeStart": "1754999938506",
    "global": "0",
    "subsid": "6",
    "cdata": "0",
    "ans": "480,31;",
    "vsig": "",
    "websig": "",
    "subcapclass": "",
    "pow_answer": "b0f2a6a5516d9f08#187",
    "pow_calc_time": "3",
    "collect": "YbPsWR48xXpeJFVD2MmCqaIBE 3xky7kedarGkKvQZXB4WPTsGldKABsxxhkhww/0xdxqB9HJKWF3RZVqEo3e49ZbUhwwvQ4mIhnSThHjvncHKl87 Fz6sPXBA5LDbZXAQipW4250HUelE6S9uWpvsBJASGKyNyu7rrDxGcgJMMciXKFr5IXem4h2u Cd2w Yu xtzzA98tdyaKfinWis/WOIbCgjQUOwUew8SNzaJB4joKePkJ4MZ9k55DC1gdr0EQNHHgGHDGRhBMkK2xvr4A7RD6AU1vNJIF5F5i25OuSLAzvSKiGnVRmbajSaOcarWd4dzzoq6wBEq9cRRF1gxYyB1HXCSkRcMJmiqlMix20Y5gKOXkFfywH0bAwLqk49tzMdJr6BVioI1y9xnTdhJK9Lnk/CfkaSxSGYi1mVLfAyPKQwVbgDH3pv/UFOrG2dZ96yVJPr54/RBVj88/nseG1wD5IkHIZTt3kzppOR7AIaTlXrz9Xo7CA RJftMFx AdSL jVyqac/LP OQaVNIWQKJFFeTX2mgjavWE4/4ZY8Fl3uYxYplcDYbkA6Mz5tZIYfQk0AQYbN0lkLcrgNLxyACnMT4vMpAqkD2y19/hPWHYce8UmXuEB70NcYnrPIDV0noTjUblzRAav71Z0Cu5bitkxP00qPeknlwthuKUWUopq6k0QZ3MzxJd/V2OArSDgiQjmeFvVUTOsZHbzQLZoZTPm/KtPm dkC2fZu5eJkXZinrNUNncAJkQ9 rWrBiVRaOflx2oTVj/Xyerw VIuhXynJt05YLJwdvVdpuH5T9vf8nxdPlfiPmK4dJIgebYyQ12Bw5/Kwf8NVDtztMrB/w1UO3O0AHPJ8csUt hzhnwQ/Z8ElTI1bpSBg5xQUalOKI5JgIYyebYwQKeBVuSirAudVTOorVvJ4d9wHlUp1ugbhokMt4T8CB lOcvssGsKeJvq91pVfzSyHgP/G 4Ybe7tOa0cfG6XRZUkTiVowpdL4Y7cC8I7uc3r9cyzVQVFqk9nCMnlPIoWrMozfZcwffzxE3NBAirL CIRYFCvfZKbhmXQGXw9h16yF5NZvUP6FyfjpDGE6SPLF5G5hx/Z4Wd TKu3kS/8rBMK712Z7aviSDG0PybTL6Qkcv8C5TyKFqzKM33y4hrfh8LllbsB662zXtC4o3n76H7QuDTQZsycsVesW1chnaNZAjIvMTbU5KlQxtBYJ5VYf6Zba8wXiDoN5hO8fc3DSt4mDfnYsUeiHuqDnuOAXu 3ugzQ5isobOi//VskrHQEfPh HhYFmAyx6L3WnTMbZjr7Lviwawp4m r3Wps6LRs51jgfqIEp2tdWTwMQkMYigbzoBVBPjJwhIF6Pa2zOKHKeRRjZi9oBZpmd13UDrdQR3y74TRxbbDvvAwuRL/ysEwrvXaYlmd4cOjVa/wqfZIvSAc0BEhJEDV7hRkcmPrSWxmYfpIiveMUyuMtFrvwE8xGKhLBrCnib6vdaTpp7Hb3QIpNYWcXTN5cGPMCw4INVSzxcQiNJlX5gOVnKuReUJCfIH8rB/w1UO3O0VJYBpAmI2TbKwf8NVDtztMrB/w1UO3O0Ieqb0C8WHCRIJmlx4O472I 80DtcKFfYISmwmuRQL0s3cKk3Lf1m9yO68GoxBgs8QC4GaHBafOZ7qB R7Yc15aERFGnGIgopKWA7uPzEwcYUV5uRCCfIIpNkpIeauG1m/iao3D Rt7f7zsYZFGjEVEsTXrMnI1UtJjhXkyUyilYcUSGzih54mxxRIbOKHnibHFEhs4oeeJscUSGzih54mxxRIbOKHnibdO024R6XRaMcUSGzih54mxxRIbOKHnibHFEhs4oeeJscUSGzih54m3TtNuEel0WjHFEhs4oeeJsRpix9zm86bHTtNuEel0Wjy5rU6H1VclHLmtTofVVyURGmLH3ObzpsSxNesycjVS0Rpix9zm86bEsTXrMnI1UtHFEhs4oeeJscUSGzih54m3TtNuEel0WjHiJ85D7K2iGnS/gCXFR7Fdf6LTa53KXA1/otNrncpcAzlL9 571uDKRjORv816xyj2/6DR2g8YCkYzkb/NescryuAsnUyXlmj2/6DR2g8YC8rgLJ1Ml5Zpjrlyi2kb0gIxLC513wkN Tscr9jxU8o8htoNtri02mIxLC513wkN/MSO/h0Dhujed5za9hQ/8j2ITo3jBah8PlAIvsb6KvxuUAi xvoq/G2ITo3jBah8PlAIvsb6KvxuUAi xvoq/GZVN Y7Hgu/cjaVmO1NS9wMtLUU TL DTy0tRT5Mv4NOY3U315aN UV0BSuYDctHuf3M02Gmd4mIiLPZ0cu24ccI7uc3r9cyz0zGK CRE4Rle2jUJ esJ/tMxivgkROEZktD39OJeALp07TbhHpdFo3TtNuEel0WjEaYsfc5vOmwcUSGzih54m0/RoTwbCZZly5rU6H1VclFLE16zJyNVLadL AJcVHsVOkQp2n68aOhu5AqcDHed6XTHFTsA dz0j2/6DR2g8YCPb/oNHaDxgHC7g0bA6IU7j2/6DR2g8YCPb/oNHaDxgMS1WJkQWDfauYV2Qn5vzdIjEsLnXfCQ3yMSwudd8JDfIxLC513wkN/2o4M/IpuEGVo4oT9PBdHWg77T tE4YZfYhOjeMFqHw9iE6N4wWofD2ITo3jBah8Pnec2vYUP/I9iE6N4wWofD2ITo3jBah8Pnec2vYUP/I9iE6N4wWofDzFIgwB2wpiZHSf1ililh2 d5za9hQ/8j2ITo3jBah8PMUiDAHbCmJkdJ/WKWKWHbnPK22lW3poHYhOjeMFqHw9iE6N4wWofD53nNr2FD/yOh7Ts2dIWKxyNpWY7U1L3AI2lZjtTUvcAZr92HxoeiVEnl5BvF4IQEy0tRT5Mv4NN/VR8jlmiYLn9VHyOWaJguF1/dxyxFd2IA6NutjZEmVH9zNNhpneJi 68kUTXWjlfLxHFBIkXkLj8TpsvC4UBO5KKsC51VM6glouudlg72/l7aNQn56wn 2w1AKZmIb5BK8kKiOCB0B17aNQn56wn 0zGK CRE4RnTMYr4JEThGSJMOR78DHJtWpOK/  6LBs8Rj34mt3L12Kdpo8svPvlHFEhs4oeeJscUSGzih54m0sTXrMnI1UtHFEhs4oeeJscUSGzih54m6dL AJcVHsV7L1jPPGgimGIKmLTbXhibtf6LTa53KXA1/otNrncpcDK0CHnbN chFI u67TJQst9xqZ9zZFZt21/z9pW2ILRJxo9N6yzHyY",
    "tlg": "3296",
    "fpinfo": "",
    "eks": "MbO5RtdXMkCoP/tKrBdmlbalnJBMBD3V29L8tdPxTt BTrfymfemnShRE0hLR9mc8qviiI983koy22d8njYpY9aUa66ZejGE9lyVXwUYuGdMyY8FcdeRRGFPrsW64AaSW6NyrkdwjYWvqKi4yyZ1AJIoZk2chWdeNMAlwzZww2tW9LBsIwjh0ErV1PWQ861qvgI0E 3bqX uaNBwXCU1rKWWUYajhXc92bWtR6cHxsk=",
    "nonce": "eda1152f11f1daf0",
    "vlg": "0_0_1",
    "vData": "VueBKpkQNbhk8PJ_PeBGU6NmzxyIi86a3y9ZJ8arLMvRp2la16iBIVmm26D8zelywuA8MwQVpcJ-wEZqtcjJ3VZ6ZTyQpe3QW-m4TuviSczvPnpDPQ2pbOKrSU8k4Ht_zjknUBsO6tifpUNwKn_V77YY"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)