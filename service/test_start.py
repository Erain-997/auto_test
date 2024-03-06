from selenium import webdriver
from testcase.test_cases import *
from configparser import ConfigParser
import pytest


class server(object):
    # def __init__(self, driver, user, password):
    #     self.driver = driver
    #     self.user = user
    #     self.password = password

    # @pytest.fixture(scope="session")  # 会话级别的 fixture，只读取一次配置
    def config_read(self):
        config = ConfigParser()
        # 读取配置文件
        files_loaded = config.read('conf/config_file.ini')
        if not files_loaded:
            print("配置文件未能正确加载")
        else:
            try:
                print(config)
                return config
            except KeyError:
                print("配置文件中填写有误")

        return None

    # 启动服务
    # @pytest.fixture(scope="function")
    def start(self):
        arg = self.config_read()
        driver = webdriver.Chrome()
        url = arg.get("out", "url")
        driver.get(url)
        user = arg.get("out", "user")
        pd = arg.get("out", "password")
        # a = {"driver": driver, "user": arg["user"], "password": arg["password"]}
        # # return driver, arg["user"], arg["password"]
        return driver, user, pd

# # 测试函数
# def test_all(start):
#     testcases = TestCases()
#     testcases.test_cases(start)
