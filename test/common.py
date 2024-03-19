from api.web import *
from api.web.assert_tools import *
# 准备各种符号和数据组合的测试数据
from test.start import *
from test import box_status
from test.login import *


def login_right(driver, user, password) -> str:
    # todo 正则优化
    clear(driver, By.ID, "login_username")
    send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
    clear(driver, By.ID, "login_password")
    send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
    click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")
    model = get_model(driver, By.XPATH,
                      "//div[@class='ant-statistic-title' and text()='型号']/following-sibling::div/span["
                      "@class='ant-statistic-content-value']")

    return model


def logout_right(driver):
    time.sleep(2)
    click(driver, By.XPATH, '//*[@id="root"]/section/header/div/a', "点击你好")
    # time.sleep(200)
    click(driver, By.XPATH, "//*[contains(text(), '登出')]", "退出登录")
    # click(driver, By.XPATH, '/html/body//div/div/ul/li/span', "退出登录")

import time
import functools

def retry(max_retries, delay=0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except AssertionError:
                    if delay > 0:
                        time.sleep(delay)
                    retries += 1
            return func(*args, **kwargs)  # Final attempt without catching AssertionError
        return wrapper
    return decorator