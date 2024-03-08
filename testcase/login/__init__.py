import time
import allure

from api.report import case_name


def send_text(driver, by, path, arg, name):
    with allure.step(name):
        element = driver.find_element(by, path)
        element.send_keys(arg)
        time.sleep(0.5)

# @case_name("输入密码")
# def send_password(driver, by, path, arg):
#     element = driver.find_element(by, path)
#     element.send_keys(arg)
#     time.sleep(0.5)
