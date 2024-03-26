from test.common import logout_right

switch_status = {True: "开启状态", False: "关闭状态"}
box_status = {True: "勾选状态", False: "未勾选状态"}

# 型号功能差异
model_network_cloud = ["H618"]
# 呼叫功能
model_call = ["S615"]

import allure
from functools import wraps
import pytest


# 定义清理函数
def cleanup(driver):
    logout_right(driver)
    driver.close()


# 注册 pytest_runtest_protocol 钩子函数
def pytest_runtest_protocol(driver):
    # 运行下一个测试用例之前执行清理函数
    cleanup(driver)

    return None
