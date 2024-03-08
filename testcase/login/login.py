from api.report import case_name
from api.tools import *
from selenium.webdriver.common.by import By
from api.web.common import *
from api.web.assert_tools import *
import pytest

# 准备各种符号和数据组合的测试数据
from testcase.login import *

test_data = [
    (generate_data_all(6), generate_data_all(6), False),  # 随机整合数据
    ("user1", "wrongpass", False),  # 错误的密码
    ("wronguser", "pass1", False),  # 错误的用户名
    # ("user1", "", False),  # 空密码
    # ("", "pass1", False),  # 空用户名
    # ("User1", "pass1", False),  # 用户名大小写敏感
    # ("user1", "Pass1", False),  # 密码大小写敏感
    # ("user1", "pass11", False),  # 密码太长
    # ("user1", "pa", False),  # 密码太短
    # ("@user1", "pass1", False),  # 用户名包含特殊字符
    # ("user1", "!pass1", False),  # 密码包含特殊字符
    # ... 可以继续添加更多的测试数据
]


@allure.step("登录测试")
def login_test(driver):
    for data in test_data:
        login(driver, data[0], data[1])
        # 校验1
        check_box(driver, By.XPATH, '//*[@id="login"]/div[4]/div/div/div/div/button', False, "记住我勾选框取消勾选")
        # 校验2
        check_text(driver, By.XPATH, '//*[@id="login_password"]', "")


def login(driver, user, password):
    send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
    send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
    res = get_box_status(driver, By.XPATH, '//*[@id="login_remember"]')
    click(driver, By.XPATH, '//*[@id="login_remember"]', "点击记住我勾选框")
    check_box(driver, By.XPATH, '//*[@id="login_remember"]', not res, "记住我勾选框状态检查,预期{}".format(str(not res)))
    click(driver, By.XPATH, '//*[@id="login"]/div[4]/div/div/div/div/button', "点击登录")
    check_element_exist(driver, By.XPATH, '//*[@id="login"]/div[4]/div/div/div/div/button', True, "校验登录-预期登录失败")
    # check_text(driver, By.XPATH, '//*[@id="root"]/header/div/a', "你好， admin")


@allure.step("正确登录")
def login_ok(driver, user, password):
    clear(driver, By.ID, "login_username")
    send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
    clear(driver, By.ID, "login_password")
    send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
    res = get_box_status(driver, By.XPATH, '//*[@id="login_remember"]')
    click(driver, By.XPATH, '//*[@id="login_remember"]', "点击记住我勾选框")
    check_box(driver, By.XPATH, '//*[@id="login_remember"]', not res, "记住我勾选框状态检查,预期{}".format(str(not res)))
    click(driver, By.XPATH, '//*[@id="login"]/div[4]/div/div/div/div/button', "点击登录")
    check_element_exist(driver, By.XPATH, '//*[@id="login"]/div[4]/div/div/div/div/button', False, "校验登录-预期登录成功")
