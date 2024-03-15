from datetime import datetime

from api.web import *
from api.web.assert_tools import *


@allure.step("升级系统")
def update_system(driver):
    click(driver, By.XPATH, '//li[5]/span', "点击常规设置->系统")


@allure.step("设备信息校验")
def check_information(driver):
    res = get_attribute_text(driver, By.XPATH, '//*[@id="root"]//div[1]/div[1]/div[2]/div[1]/div')
    print(datetime.now(), ": ", res, "-----------")
