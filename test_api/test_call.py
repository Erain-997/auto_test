from api.http.login import api_login
from api.http.state import api_sip_registration_status


# todo 可能做成服务的形式提供
class TestApi:
    def test_call(self):
        url = "http://192.168.57.196"
        res = api_login(url)
        se = res['data']['SessionID'].strip()
        api_sip_registration_status(url, se)
