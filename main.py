import pytest
import shutil
from api.ding import send_message_to_ding
from api.report import *


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
    pytest.main(['-s', '-v', '--alluredir=./allure-results', "testcase/"])
    # 生成报告
    generate_report()
    # 获取报告地址
    url = get_report_url()
    # print("目标网址: ", url)
    # 钉钉推送
    # send_message_to_ding(url)
