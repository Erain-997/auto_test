import allure
from allure_commons.types import AttachmentType
from selenium.common import exceptions
import logging

# 校验勾选框
from log import log_info


# todo 错误截图
def check_box(driver, by, path, status, name):
    with allure.step(name):
        element = driver.find_element(by, path)
        assert element.is_selected() == status, name + "失败"

    #     # 附加截图或其他文件作为结果记录
    # with allure.attach("Calculation Result", "text/plain") as attachment:
    #     attachment.add_file(states, file_name="result.txt", attachment_type=AttachmentType.TEXT)


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
                assert res, name + "失败,预期:{},实际:{}".format(data[states], data[res])
            except AssertionError:
                log_info("文本校验失败" + str(element))
        except exceptions.NoSuchElementException:
            log_info("查找元素失败")
            pass
    # element = driver.find_element(by, path)
    # print(element)
    # assert element == states, "测试失败"


# 校验文本
def check_text(driver, by, path, expect):
    with allure.step("检查文本框内容,预期:{}".format(expect)):
        element = driver.find_element(by, path)
        fact_text = element.get_attribute("value")
        try:
            assert fact_text == expect, "校验文本失败,预期:{},实际:{}".format(expect, fact_text)
        except AssertionError:
            pass


def check_element_true(driver, by, arg):
    element = driver.find_element(by, arg)
    assert element == True, "测试失败"
