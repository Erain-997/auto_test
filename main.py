import pytest
import shutil
from api.ding import send_message_to_ding
from api.http.http import api_login
from api.report import *
from api.ssh import ssh_connect
from api.telnet import *


def clear():
    dir_path = ['./allure-results', './reports']
    for i in dir_path:
        if os.path.exists(i):
            shutil.rmtree(i)
        os.mkdir(i)


if __name__ == '__main__':
    # 环境清理
    clear()
    # 启动
    pytest.main(
        ['-s', '-v','--capture=no',"--continue-on-collection-errors", '--alluredir=./allure-results', "test/"])
    time.sleep(2)
    # 生成报告
    generate_report()
    time.sleep(2)
    # 获取报告地址
    url = get_report_url()
    # print("目标网址: ", url)
    #
    # # 钉钉推送 todo 优化模块名称
    # # send_message_to_ding(url)

    # telnet_ls("192.168.57.200", "9900", "root", "1234321")

    # api_login()
