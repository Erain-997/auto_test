import allure
from allure_commons.types import AttachmentType
from selenium.common import exceptions
import logging

# 校验勾选框
from selenium.webdriver.common.by import By

from log import log_info

# todo 错误截图
from testcase import *


def check_box(driver, by, path, status, name):
    with allure.step(name):
        try:
            element = driver.find_element(by, path)
            log_info("勾选框校验状态校验成功{},用例:{}".format(element.is_selected() == status, name))
            assert element.is_selected() == status
        except AssertionError as e:
            assert False, name+", 断言失败, 实际:{}".format(box_status[element.is_selected()])
    #     # 附加截图或其他文件作为结果记录
    # with allure.attach("Calculation Result", "text/plain") as attachment:
    #     attachment.add_file(states, file_name="result.txt", attachment_type=AttachmentType.TEXT)


def check_switch(driver, by, path, status, name):
    with allure.step(name):
        try:
            switch = driver.find_element(by, path)
            is_checked = 'ant-switch-checked' in switch.get_attribute('class')
            log_info("开关按钮校验状态校验预期:{},实际:{}".format(status, is_checked))
            assert is_checked == status
        except AssertionError as e:
            assert False, name+"断言失败, 实际:{}".format(switch_status[is_checked])


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
                log_info("文本校验失败" + str(element))
                assert res, name + "失败,预期:{},实际:{}".format(data[states], data[res])
        except exceptions.NoSuchElementException:
            if states:
                log_info("查找元素失败", path)
                assert res, name + "查找元素失败,path:{}, 预期:{},实际:{}".format(path,data[states], data[res])
            pass
    # element = driver.find_element(by, path)
    # print(element)
    # assert element == states, "测试失败"


# 校验文本
def check_text(driver, by, path, expect):
    with allure.step("检查文本框内容,预期:{}".format(expect)):
        element = driver.find_element(by, path)
        fact_text = ""
        if by == By.ID:
            fact_text = element.get_attribute("value")
        else:
            fact_text = element.text
        try:
            assert fact_text == expect
        except AssertionError:
            print("文本校验{}失败,预期:{}:,实际:{}".format(path, expect, fact_text))
            assert False, "文本校验{}失败,预期:{}:,实际:{}".format(path, expect, fact_text)
            pass


def check_element_true(driver, by, arg):
    element = driver.find_element(by, arg)
    if element:
        assert True, "元素存在, 断言成功"
    else:
        assert False, "元素存在, 用例失败, 预期元素不存在"


