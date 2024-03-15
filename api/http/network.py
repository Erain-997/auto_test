import json
import requests


def api_set_network_configuration(url, session_id, dhcp_status: bool):
    """
    :param url:
    :param session_id:
    :param dhcp_status: True, False
    :return:
    """
    api_path = "/api/v1/network/settings"

    payload = json.dumps({
        "dhcp": dhcp_status
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)


def api_set_ntp_configuration(url, session_id, enabled: bool, server):
    """
    :param url:
    :param session_id:
    :param enabled:
    :param server:
    :return:
    """
    api_path = "/api/v1/network/ntp"

    payload = json.dumps({
        "enabled": enabled,
        "server": server
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)
