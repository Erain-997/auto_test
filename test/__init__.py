switch_status = {True: "开启状态", False: "关闭状态"}
box_status = {True: "勾选状态", False: "未勾选状态"}

# 型号功能差异
model_network_cloud = ["H618"]

import allure
from functools import wraps


def handle_failure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AssertionError as e:
            driver = args[0]
            with allure.step("{} 用例失败".format(func.__name__)):
                allure.attach(driver.get_screenshot_as_png(), name="失败截图", attachment_type=allure.attachment_type.PNG)
                allure.attach(str(e), name="失败原因", attachment_type=allure.attachment_type.TEXT)
            # 执行其他操作，例如记录日志等
            pass

    return wrapper
