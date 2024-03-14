import http.client


def api_login():
    conn = http.client.HTTPSConnection("http://192.168.57.200/")
    payload = ''
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }
    conn.request("GET", "/api/v1/login?username=admin&password=%7B%7B'123456'%7Cmd5%7D%7D", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
