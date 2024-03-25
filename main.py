import pytest
import shutil
from api.ding import send_message_to_ding
from api.http.state import api_sip_registration_status
from api.report import *
from api.telnet import *
from test_api.test_call import TestApi


def clear():
    dir_path = ['./allure-results', './reports']
    for i in dir_path:
        if os.path.exists(i):
            shutil.rmtree(i)
        os.mkdir(i)


if __name__ == '__main__':
    # todo 登录现在限制10个接口
    # 环境清理
    clear()
    # # 启动
    pytest.main(
        ['-s', '-v', '--capture=no', "--continue-on-collection-errors", '--alluredir=./allure-results',
         "test/", "--reruns", "0"])
    time.sleep(2)
    # 生成报告
    generate_report()
    time.sleep(2)
    # 获取报告地址
    url = get_report_url()
    print("目标网址: ", url)

    # 钉钉推送 todo 优化模块名称
    # send_message_to_ding(url)
    # telnet_ls("192.168.57.200", "9900", "root", "1234321")

    # a = TestApi()
    # a.test_call()
