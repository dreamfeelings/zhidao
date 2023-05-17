import requests


headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Origin": "https://studyvideoh5.zhihuishu.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://studyvideoh5.zhihuishu.com/stuStudy?recruitAndCourseId=4b5e5c5d45584859454a5859584d504658",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
url = "https://appcomm-user.zhihuishu.com/app-commserv-user/c/has"
params = {
    "uid": "jMYPGoXymBRwoH+rrkr/4zatV2fEMKo8O6ycqrNm2nkJy2hm1vIYdhr0dxgkBfQ86tuyHTkqF2sX/ukOB6wslqzWnH6kxZykmDG4EvQZuquSTFp5S7cAxTWLWzqkiyFuqBAAsm5djilSM32DbhrxeKzyDphLHMxLRaRkCmsYoko="
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)