from selenium.webdriver import ActionChains

from api.report import case_name
from api.tools import *
from selenium.webdriver.common.by import By
from api.web import *
from api.web.assert_tools import *
import pytest

# 准备各种符号和数据组合的测试数据
from testcase import box_status
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
        # check_box(driver, By.XPATH, '//*[@id="login"]/div[4]/div/div/div/div/button', False, "点击记住我勾选框")
        # 校验2
        check_text(driver, By.XPATH, '//*[@id="login_password"]', "")


def login(driver, user, password):
    send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
    send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
    res = get_box_status(driver, By.XPATH, '//*[@id="login_remember"]')
    click(driver, By.XPATH, '//*[@id="login_remember"]', "点击记住我勾选框")
    check_box(driver, By.XPATH, '//*[@id="login_remember"]', not res, "记住我勾选框状态检查,预期{}".format(box_status[not res]))
    click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")
    check_element_exist(driver, By.XPATH, '//*[@id="login"]/div[4]/div/div/div/div/button', True, "校验登录-预期登录失败")
    # check_text(driver, By.XPATH, '//*[@id="root"]/header/div/a', "你好， admin")


@allure.step("正确登录-默认不记住我")
def login_ok(driver, user, password, remember=True):
    clear(driver, By.ID, "login_username")
    send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
    clear(driver, By.ID, "login_password")
    send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
    res = get_box_status(driver, By.XPATH, '//*[@id="login_remember"]')
    if remember and not res:
        click(driver, By.XPATH, '//*[@id="login_remember"]', "点击记住我勾选框")
        check_box(driver, By.XPATH, '//*[@id="login_remember"]', not res, "记住我勾选框状态检查,预期{}".format(box_status[not res]))
    # todo 正则 driver.find_element_by_xpath('//button[contains(.,"Sign in")]')
    click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")
    check_element_exist(driver, By.XPATH, "//*[contains(text(), '设备')]", True, "校验登录-预期登录成功")


@allure.step("退出登录-记住我")
def login_out_check_remember(driver, user, password, login_end=True):
    click(driver, By.XPATH, '//*[@id="root"]/section/header/div/a', "点击你好")
    click(driver, By.XPATH, '/html/body/div[2]/div/div/ul/li/span', "退出登录")
    time.sleep(1)
    check_box(driver, By.XPATH, '//*[@id="login_remember"]', True, "记住我勾选框状态检查,预期{}".format(box_status[True]))
    check_text(driver, By.ID, "login_username", "admin")
    click(driver, By.XPATH, '//*[@id="login_remember"]', "取消记住我勾选框")
    click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")


@allure.step("退出登录-不记住我")
def login_out_check_not_remember(driver, user, password, login_end=True):
    click(driver, By.XPATH, '//*[@id="root"]/section/header/div/a', "点击你好")
    click(driver, By.XPATH, '/html/body/div[2]/div/div/ul/li/span', "退出登录")
    time.sleep(1)
    check_box(driver, By.XPATH, '//*[@id="login_remember"]', False, "记住我勾选框状态检查,预期{}".format(box_status[False]))
    check_text(driver, By.ID, "login_username", "")
    send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
    send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
    click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")


@allure.step("登录语言")
def login_language(driver):
    # text = get_text(driver, By.XPATH, "/html/body/div[2]//div[2]//div[2]/div")

    # 定位下拉框元素
    click(driver, By.XPATH, '//*[@id="root"]/div//div/div[1]/div/div/div/span[2]', "登录界面点击语言")
    click(driver, By.XPATH, '/html/body/div[2]//div[2]/div[1]/div/div/div[1]/div', "切换成English")
    time.sleep(1.5)
    check_text(driver, By.XPATH, '//*[@id="login"]/div[4]//div/button/span', 'Sign in')

    click(driver, By.XPATH, '//*[@id="root"]/div//div/div[1]/div/div/div/span[2]', "登录界面点击语言")
    click(driver, By.XPATH, '/html/body/div[2]//div[2]//div[2]/div', "切换成中文")
    time.sleep(1.5)
    check_text(driver, By.XPATH, '//*[@id="login"]/div[4]//div/button/span', "登 录")

    # input()


@allure.step("切换语言")
def change_language(driver):
    # 获取焦点
    # dropdown = driver.find_element(By.XPATH, '//*[@id="root"]/section/header//button/span[2]')
    # # 使用鼠标移动到下拉框元素，使其获得焦点
    # actions = ActionChains(driver)
    # actions.move_to_element(dropdown).perform()

    # 定位下拉框元素
    click(driver, By.XPATH, '//*[@id="root"]/section/header//button/span[2]', "点击语言")
    click(driver, By.XPATH, '/html/body/div[2]//ul/li[1]/span', "切换成中文")
    check_text(driver, By.XPATH, '//*[@id="root"]//li[1]//span[2]', "常规设置")
    time.sleep(1.5)
    click(driver, By.XPATH, '//*[@id="root"]/section/header//button/span[2]', "点击语言")
    click(driver, By.XPATH, '/html/body/div[2]//ul/li[2]/span', "切换成英文")
    time.sleep(1.5)
    check_text(driver, By.XPATH, '//*[@id="root"]//li[1]//span[2]', "General")
    # input()
