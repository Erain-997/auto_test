import time
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from api.report import case_name


def get_box_status(driver, by, arg):
    element = driver.find_element(by, arg)
    return element.is_selected()

# todo
def get_button_status(driver, by, arg):
    element = driver.find_element(by, arg)
    return element.is_enabled()


def get_switch_status(driver, by, arg):
    switch = driver.find_element(by, arg)
    is_checked = 'ant-switch-checked' in switch.get_attribute('class')
    return is_checked


def get_text(driver, by, path):
    text = ""
    try:
        element = driver.find_element(by, path)
        text = element.get_attribute("value")
    except AssertionError:
        print("获取文本{}失败".format(path))
        pass
    return text


def click(driver, by, arg, name="点击(默认)"):
    with allure.step(name):
        element = driver.find_element(by, arg)
        if element:
            element.click()
        time.sleep(0.5)


@case_name("清空文本")
def clear(driver, by, arg):
    element = driver.find_element(by, arg)
    element.send_keys(Keys.CONTROL + "a")  # 全选文本
    element.send_keys(Keys.BACKSPACE)  # 删除选中的文本
    time.sleep(0.5)
