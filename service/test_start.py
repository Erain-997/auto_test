from selenium import webdriver
from testcase.test_cases import *
from configparser import ConfigParser
import pytest
from log import log_info


class Server(object):
    # todo 设置成环境变量, 第一层
    # @pytest.fixture(scope="session")  # 会话级别的 fixture，只读取一次配置
    def config_read(self):
        config = ConfigParser()
        # 读取配置文件
        files_loaded = config.read('conf/config_file.ini')
        if not files_loaded:
            log_info("配置文件未能正确加载")
        else:
            try:
                log_info("config配置", config)
                return config
            except KeyError:
                log_info("配置文件中填写有误")

        return None

    # 启动服务
    # @pytest.fixture(scope="function")
    def start(self):
        # 优化成传参
        # todo 多设备操作
        equipment = "out"
        arg = self.config_read()
        driver = webdriver.Chrome()
        url = arg.get(equipment, "url")
        user = arg.get(equipment, "user")
        pd = arg.get(equipment, "password")
        driver.get(url)
        return driver, user, pd
