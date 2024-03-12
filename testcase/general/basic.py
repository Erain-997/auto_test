from api.web import *
from api.web.assert_tools import *


@allure.step("升级系统")
def update_system(driver):
    click(driver, By.XPATH, '//li[2]/span', "点击常规设置->基础设置")

