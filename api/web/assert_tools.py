import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import exceptions
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from log import log_info
from selenium.common import NoSuchElementException, TimeoutException
from test import *


def allure_attach(driver, path, fail_text):
    allure.attach(driver.get_screenshot_as_png(), name=fail_text, attachment_type=allure.attachment_type.PNG)
    allure.attach(path, name="xpath路径: ", attachment_type=allure.attachment_type.TEXT)
    pytest.fail(fail_text)


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
    #     # 附加截图或其他文件作为结果记录
    # with allure.attach("Calculation Result", "text/plain") as attachment:
    #     attachment.add_file(states, file_name="result.txt", attachment_type=AttachmentType.TEXT)


def check_switch(driver, by, path, status, name):
    time.sleep(1)
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


# 校验元素是否存在
def check_element_exist(driver, by, path, states, name):
    data = {True: "存在", False: "不存在"}
    with allure.step(name):
        try:
            element = driver.find_element(by, path)
            if element:
                res = True
            else:
                res = False
            try:
                assert res
            except AssertionError:
                log_info("元素校验失败" + str(element))
                assert res, name + "失败,预期:{},实际:{}".format(data[states], data[res])
        except exceptions.NoSuchElementException:
            if states:
                log_info("查找元素失败", path)
                assert res, name + "查找元素失败,path:{}, 预期:{},实际:{}".format(path, data[states], data[res])


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
