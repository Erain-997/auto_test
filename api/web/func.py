from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from api.report import case_name
from api.web.assert_tools import *


def get_model(driver, by, path):
    try:
        # 等待设备型号元素加载完成
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, path)))
        return element.text
    except TimeoutException as t:
        with allure.step("设备登录失败, 获取型号超时"):
            allure_attach(driver, path, "设备登录失败, 获取型号超时" + str(t))

    return "型号错误"


def get_box_status(driver, by, path, name):
    try:
        # 等待设备型号元素加载完成
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, path)))
        return element.is_selected()
    except TimeoutException as e:
        with allure.step(name + "勾选框状态获取失败"):
            allure.attach(driver.get_screenshot_as_png(), name=name + "勾选框状态获取失败",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(path, name="xpath路径", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(name + "勾选框状态获取失败" + str(e))

    # return element.is_selected()


# todo
def get_button_status(driver, by, arg):
    # 等待设备型号元素加载完成
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, arg)))
    return element.is_enabled()


def get_switch_status(driver, by, path, name):
    try:
        # 等待设备型号元素加载完成
        switch = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, path)))
        return 'ant-switch-checked' in switch.get_attribute('class')
    except TimeoutException as e:
        with allure.step(name + "开关按钮状态获取失败"):
            allure.attach(driver.get_screenshot_as_png(), name=name + "开关按钮状态获取失败",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(path, name="xpath路径", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(name + "开关按钮状态获取失败" + str(e))


def get_attribute_text(driver, by, path, name) -> str:
    try:
        element = driver.find_element(by, path)
        text = element.get_attribute("value")
        return text
    except AssertionError as e:
        with allure.step(name + "文本获取失败"):
            allure.attach(driver.get_screenshot_as_png(), name=name + "文本获取失败",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(path, name="xpath路径", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(name + "文本获取失败" + str(e))


def click(driver, by, path, name="点击(默认)"):
    with allure.step(name):
        try:
            element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((by, path)))
            if element:
                element.click()
            time.sleep(0.5)
            return element
        except TimeoutException as t:
            allure_attach(driver, path, name + "获取元素失败" + str(t))


@case_name("清空文本")
def clear(driver, by, path):
    try:
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((by, path)))
        element.send_keys(Keys.CONTROL + "a")  # 全选文本
        element.send_keys(Keys.BACKSPACE)  # 删除选中的文本
    except TimeoutException as t:
        allure_attach(driver, path, path + "清空文本失败" + str(t))

