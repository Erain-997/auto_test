import hashlib
import json
import requests


def api_login(url):
    """
    :param url: http://192.168.57.200/
    :return:
    """
    api_path = "/cgi-bin/webapi.cgi?api=login&username=admin&password=e10adc3949ba59abbe56e057f20f883e"
    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }
    # md5_password = hashlib.md5(password.encode()).hexdigest()  # 将密码转换为 MD5
    response = requests.request("GET", url + api_path, headers=headers, data=payload)
    if len(response.cookies) > 0:
        print("新服务器SessionId:", response.cookies["SessionID"].strip())
        return response.cookies["SessionID"].strip()
    # 解析 JSON 数据
    print(response.text, 11)
    response_json = json.loads(response.text)
    print("旧服务器SessionId:", response_json['data']['SessionID'].strip())
    return response_json['data']['SessionID'].strip()
