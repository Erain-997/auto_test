import json
import requests


def api_sip_registration_status(url, session_id):
    """
    :param url: http://192.168.57.200/
    :param session_id:
    :return:
    """
    api_path = "/api/v1/sip/status"

    payload = json.dumps({

    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("GET", url + api_path, headers=headers, data=payload)
    print(response.text)
