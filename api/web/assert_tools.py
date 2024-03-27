import base64
import time
import allure
import pytest
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from log import log_info
from selenium.common import TimeoutException


def allure_attach(driver, path, fail_text):
    allure.attach(driver.get_screenshot_as_png(), name=fail_text, attachment_type=allure.attachment_type.PNG)
    allure.attach(path, name="xpath路径: ", attachment_type=allure.attachment_type.TEXT)
    pytest.fail(fail_text)


# todo 拼接失败, 取多次上传
def capture_full_page_screenshot(driver, full=True):
    # 获取网页内容高度
    page_height = driver.execute_script("return document.body.scrollHeight")
    # # 设置浏览器窗口大小与网页内容高度一致
    # driver.set_window_size(driver.get_window_size()['width'], page_height)
    # 初始化截图列表
    screenshots = []
    # full_screenshot = b''
    # 计算滚动步长
    scroll_step = driver.get_window_size()['height']
    # 滚动窗口并截取每个视图的截图
    for y in range(0, page_height, scroll_step):
        time.sleep(0.5)
        # 滚动窗口
        driver.execute_script("window.scrollTo(0, {});".format(y))
        # 等待页面滚动完成
        time.sleep(0.5)
        # 截取当前视图的截图
        # screenshot = driver.get_screenshot_as_png()
        # screenshots.append(screenshot)

        allure.attach(driver.get_screenshot_as_png(), name=str(scroll_step), attachment_type=allure.attachment_type.PNG)
        if not full:
            return
            # full_screenshot += driver.get_screenshot_as_png()
    # 创建完整截图
    # full_screenshot = b''.join(screenshots)
    # 将长图转换为 Base64 编码
    # screenshot_base64 = base64.b64encode(full_screenshot).decode('utf-8')
    # allure.attach(full_screenshot, name=str(page_height + 100), attachment_type=allure.attachment_type.PNG)

    # return full_screenshot


def check_box(driver, by, path, status, name):
    with allure.step(name):
        try:
            element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((by, path)))
            log_info("勾选框校验状态校验成功{},用例:{}".format(element.is_selected() == status, name))
            try:
                assert element.is_selected() == status
            except AssertionError as e:
                with allure.step(name + "勾选框状态校验失败"):
                    allure_attach(driver, path, name + "勾选框状态校验失败" + str(e))
        except TimeoutException as t:
            with allure.step(name + "勾选框状态获取失败"):
                allure_attach(driver, path, name + "勾选框状态获取失败" + str(t))


def check_save_success(driver, name):
    with allure.step(name):
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '保存成功')]")))
        except TimeoutException as t:
            with allure.step(name + "没弹出保存成功Tips, 请检查"):
                allure_attach(driver, "//*[contains(text(), '保存成功')]", name + ",保存成功Tips状态获取元素失败" + str(t))

        capture_full_page_screenshot(driver, False)


def check_switch(driver, by, path, status, name):
    # time.sleep(1)
    with allure.step(name):
        try:
            switch = WebDriverWait(driver, 3).until(EC.presence_of_element_located((by, path)))
            is_checked = 'ant-switch-checked' in switch.get_attribute('class')
            try:
                assert is_checked == status
            except AssertionError as e:
                with allure.step(name + "开关状态校验失败"):
                    allure_attach(driver, path, name + ",开关状态校验失败" + str(e))
        except TimeoutException as t:
            with allure.step(name + "开关状态获取元素失败"):
                allure_attach(driver, path, name + ",开关状态获取元素失败" + str(t))
        # 截图
        capture_full_page_screenshot(driver)


# 校验元素是否存在
def check_element_exist(driver, by, path, name):
    with allure.step(name):
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((by, path)))
        except TimeoutException as t:
            allure_attach(driver, path, name + "获取元素失败" + str(t))

    # data = {True: "存在", False: "不存在"}
    # with allure.step(name):
    #     try:
    #         element = driver.find_element(by, path)
    #         if element:
    #             res = True
    #         else:
    #             res = False
    #         try:
    #             assert res
    #         except AssertionError:
    #             log_info("元素校验失败" + str(element))
    #             assert res, name + "失败,预期:{},实际:{}".format(data[states], data[res])
    #     except exceptions.NoSuchElementException:
    #         if states:
    #             log_info("查找元素失败", path)
    #             assert res, name + "查找元素失败,path:{}, 预期:{},实际:{}".format(path, data[states], data[res])


# 校验文本
def check_text(driver, by, path, expect):
    with allure.step("检查文本框内容,预期:{}".format(expect)):
        try:
            element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((by, path)))
            fact_text = element.text
            try:
                assert fact_text == expect
            except AssertionError as e:
                with allure.step("文本内容校验失败,预期:{},实际{}".format(expect, fact_text)):
                    allure_attach(driver, path, "文本内容校验失败,预期:{},实际{}.".format(expect, fact_text) + str(e))
        except TimeoutException as t:
            with allure.step("文本状态获取失败,获取不到:{}".format(expect)):
                allure_attach(driver, path, "文本状态获取失败,获取不到:{}.".format(expect) + str(t))


# 校验文本
def check_text_value(driver, by, path, expect):
    with allure.step("检查文本框内容,预期:{}".format(expect)):
        try:
            element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((by, path)))
            fact_text = element.get_attribute("value")
            try:
                assert fact_text == expect
            except AssertionError as e:
                with allure.step("文本内容校验失败,预期:{},实际{}".format(expect, fact_text)):
                    allure_attach(driver, path, "文本内容校验失败,预期:{},实际{}.".format(expect, fact_text) + str(e))
        except TimeoutException as t:
            with allure.step("文本状态获取失败,获取不到:{}".format(expect)):
                allure_attach(driver, path, "文本状态获取失败,获取不到:{}.".format(expect) + str(t))


def check_element_true(driver, by, arg):
    element = driver.find_element(by, arg)
    if element:
        assert True, "元素存在, 断言成功"
    else:
        assert False, "元素存在, 用例失败, 预期元素不存在"
