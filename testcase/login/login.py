from api.tools import *
from selenium.webdriver.common.by import By
from api.web.common import *
from api.web.assert_tools import *
import pytest

# 准备各种符号和数据组合的测试数据
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


def login_test(driver):
    for data in test_data:
        login(driver, data[0], data[1])
        check_box(driver, By.XPATH, '//*[@id="login"]/div[4]/div/div/div/div/button',False)


def login(driver, user, password):
    # 输入用户名
    send(driver, By.ID, "login_username", user)
    # 输入密码
    send(driver, By.ID, "login_password", password)
    res = check_box_status(driver, By.XPATH, '//*[@id="login_remember"]')
    # 勾选
    click(driver, By.XPATH, '//*[@id="login_remember"]')
    check_box(driver, By.XPATH, '//*[@id="login_remember"]', not res)
    # 登录
    click(driver, By.XPATH, '//*[@id="login"]/div[4]/div/div/div/div/button')
