import http.client


def api_login2():
    conn = http.client.HTTPConnection("192.168.57.200")
    payload = ''
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }
    conn.request("GET", "", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    print(data.decode("utf-8"))


import requests


def api_login():
    url = "http://192.168.57.200/api/v1/login?username=admin&password={{'123456'|md5}}"

    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response)
    print(response.text)
