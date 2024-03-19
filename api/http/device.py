import json
import os
import re

import requests


def api_set_the_current_device_language(url, session_id):
    """
    只允许设置成中文
    :param url:
    :param session_id:
    :return:
    """
    api_path = "/api/v1/device/language"

    payload = json.dumps({
        "language": "简体中文"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)


def api_set_current_device_configuration(url, session_id, panel_mode, building: int, unit: int, floor: int,
                                         apartment: int, device_number: int,
                                         no_unit: bool):
    """
    :param url:
    :param session_id:
    :param panel_mode:Allowed values:Unit, Gate Station, Villa
    :param building: >= 0,<= 999
    :param unit: >= 0,<= 99
    :param floor: >= 0,<= 98
    :param apartment: >= 0,<= 99
    :param device_number: >= 0,<= 9
    :param no_unit:
    :return:
    """
    api_path = "/api/v1/device/settings"

    payload = json.dumps({
        "panel_mode": panel_mode,
        "building": building,
        "unit": unit,
        "floor": floor,
        "apartment": apartment,
        "device_number": device_number,
        "no_unit": no_unit
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)


def api_set_sip_configuration_items(url, session_id, proxy, outbound, transport, display_name, username, register_name,
                                    password):
    """
    :param url:
    :param session_id:
    :param proxy:
    :param outbound:
    :param transport: Allowed values: UDP TCP TLS
    :param display_name:
    :param username:
    :param register_name:
    :param password:
    :return:
    """
    api_path = "/api/v1/device/sip/settings"

    payload = json.dumps({
        "proxy": proxy,
        "outbound": outbound,
        "transport": transport,
        "display_name": display_name,
        "username": username,
        "register_name": register_name,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)


def api_set_device_video_configuration(url, session_id, video_resolution):
    """
    :param url:
    :param session_id:
    :param video_resolution: "640x480"
    :return:
    """
    api_path = "/api/v1/device/video/settings"

    payload = json.dumps({
        "video_resolution": video_resolution
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)


def api_set_device_volume(url, session_id, talk_volume: int, system_volume: int):
    """
    :param url:
    :param session_id:
    :param talk_volume: >= 1, <= 6
    :param system_volume: >= 1, <= 6
    :return:
    """
    api_path = "/api/v1/device/volume/settings"

    payload = json.dumps({
        "talk_volume": talk_volume,
        "system_volume": system_volume
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)


def api_set_up_device_management_card(url, session_id, card, enabled: bool):
    """
    :param url:
    :param session_id:
    :param card:
    :param enabled:
    :return:
    """
    api_path = "/api/v1/access/card/master"

    payload = json.dumps({
        "card": card,
        "enabled": enabled
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)


def api_set_sip_switch_configuration(url, session_id, sip_enable: bool):
    """
    :param url:
    :param session_id:
    :param sip_enable:
    :return:
    """
    api_path = "/api/v1/device/sip/enable"

    payload = json.dumps({
        "sip_enable": sip_enable
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data=payload)
    print(response.text)


def api_capture_pcap_start(url, session_id):
    """
    :param url:
    :param session_id:
    :return:
    """
    api_path = "/cgi-bin/webapi.cgi?api=capture"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': "SessionID=" + session_id
    }

    response = requests.request("POST", url + api_path, headers=headers, data={"action": "1"})

    # 解析 JSON 数据
    response_json = json.loads(response.text)
    return response_json


def api_capture_pcap_end(url, session_id):
    """
    :param url:
    :param session_id:
    :return:
    """
    api_path = "/cgi-bin/webapi.cgi?api=capture"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie': "SessionID=" + session_id
    }
    response = requests.request("POST", url + api_path, headers=headers, data={"action": "0"})
    # 解析 JSON 数据
    response_json = json.loads(response.text)
    return response_json


def api_download_pcap(url, session_id, name):
    """
    :param url:
    :param session_id:
    :return:
    """
    # api_path = "/data/packet.pcap"
    headers = {
        'Content-Type': 'text/plain; charset=utf-8',
        'Cookie': "SessionID=" + session_id
    }
    response = requests.get(url + name, headers=headers, stream=True)
    pcapname = filename = re.search(r'[^/]+$', name).group(0)
    save_path = os.path.expanduser('~/Desktop/' + pcapname)
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    print("抓包成功:", '~/Desktop/' + pcapname)
