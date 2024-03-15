import json
import requests


def api_control_device_to_initiate_a_call(url, session_id, dial_mode: str, dial_id: str):
    """
    :param url: http://192.168.57.200/
    :param session_id:
    :param dial_mode: ip, sip, roomNo
    :param dial_id: 192.168.57.200
    :return:
    """
    api_path = "/api/v1/call/start"

    payload = json.dumps({
        "dial_mode": dial_mode,
        "dial_id": dial_id
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)


def api_control_the_device_to_end_the_current_call(url, session_id):
    """
    :param url:
    :param session_id:
    :return:
    """
    api_path = "/api/v1/call/end"

    payload = json.dumps({

    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)
