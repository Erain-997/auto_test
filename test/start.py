import allure_commons
from selenium import webdriver
from selenium.common import NoSuchWindowException

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


@pytest.fixture(scope="class")
def driver(request):
    # 在每个测试用例之前创建一个新的driver对象
    driver_instance = webdriver.Chrome()
    # 创建 Chrome Options 对象
    options = webdriver.ChromeOptions()
    # 最大化浏览器窗口
    options.add_argument("--start-maximized")
    # 将 Options 对象传递给 WebDriver
    driver_instance = webdriver.Chrome(options=options)
    # 添加一个finalizer，确保每个测试用例结束后关闭当前标签页
    def close_tab():
        try:
            # 关闭当前标签页
            driver_instance.close()
        except NoSuchWindowException:
            # 如果关闭后出现NoSuchWindowException，切换到其他窗口
            handles = driver_instance.window_handles
            driver_instance.switch_to.window(handles[-1])  # 切换到最后一个窗口

    request.addfinalizer(close_tab)

    return driver_instance


# 启动服务
def start():
    # 优化成传参
    # todo 多设备操作
    equipment = "out"
    arg = config_read()
    url = arg.get(equipment, "url")
    user = arg.get(equipment, "user")
    pd = arg.get(equipment, "password")
    # driver = webdriver.Chrome()
    # driver.get(url)

    # log_info("sessionID", driver.session_id)
    return [(url, user, pd)]


# @pytest.fixture(scope="function")
def start_case(driver, url):
    # todo 可能有用
    # driver = webdriver.Remote(command_executor=url, desired_capabilities={}, session_id=session_id)
    # 切换到其他窗口后执行JavaScript脚本
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])  # 切换到最后一个窗口
    # 打开新的标签页
    driver.execute_script("window.open();")
    # 切换到新打开的标签页
    driver.switch_to.window(driver.window_handles[-1])
    # 在新标签页中进行操作，例如访问某个网页
    driver.get(url)
