import time
from api.http.communication import api_control_device_to_initiate_a_call
from api.http.device import *
from api.http.login import api_login
from api.http.state import api_sip_registration_status


# todo 可能做成服务的形式提供
class TestApi:
    def test_call(self):
        url = "http://192.168.57.196"
        res = api_login(url)
        api_control_device_to_initiate_a_call(url, res, "ip", "192.168.57.200")

    def test_pcap(self):
        url = "http://192.168.57.200"
        # url = "http://192.168.57.200"
        res = api_login(url)
        api_capture_pcap_start(url, res)
        time.sleep(3)
        name = api_capture_pcap_end(url, res)
        api_download_pcap(url, res, name["file_name"])
