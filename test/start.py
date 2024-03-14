import allure_commons
from selenium import webdriver
from test.common import *
from configparser import ConfigParser
import pytest
from log import log_info
import allure
from allure_commons.types import AttachmentType


def config_read():
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
# @pytest.fixture
def start():
    # 优化成传参
    # todo 多设备操作
    equipment = "out"
    arg = config_read()
    driver = webdriver.Chrome()
    url = arg.get(equipment, "url")
    user = arg.get(equipment, "user")
    pd = arg.get(equipment, "password")
    driver.get(url)
    return driver, user, pd
