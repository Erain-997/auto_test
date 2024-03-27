import allure
import pytest
from selenium.webdriver.common.by import By

from test import model_network_cloud, switch_status
from test.common import login_right, logout_right
from test.start import *


@allure.feature("对讲设置-网络")
@allure.description("网络测试")
@pytest.mark.parametrize("ip, user, password", start())
class TestNetwork:
    # @allure.story("dhcp设置")
    # def network_dhcp(self):
    #     driver, user, password = start()
    #     click(driver, By.XPATH, '//*[@id="root"]//li[1]//span[2]', "点击收起常规设置")
    #     click(driver, By.XPATH, '//*[@id="root"]//li[2]//span[2]', "点击安防管理")
    #     click(driver, By.XPATH, "(//*[contains(text(), '网络')])[2]", "点击网络")
    #     res = get_switch_status(driver, By.XPATH, '//*[@id="network_dhcp"]', "dhcp")
    #     click(driver, By.XPATH, '//*[@id="network_dhcp"]', "点击dhcp按钮")
    #     res = get_switch_status(driver, By.XPATH, '//*[@id="network_dhcp"]', "dhcp")
    #     # todo 没加保存, 保存后丢失目标

    @allure.story("网络-CMS")
    @allure.title("CMS启用和关闭,测试设备:{ip}")
    def test_cms(self, driver, ip, user, password):
        start_case(driver, ip)
        model = login_right(driver, user, password)
        # if model not in model_network_cloud:
        #     allure.step("当前型号{},没有网络-CMS功能".format(model))
        #     return
        click(driver, By.XPATH, "//*[contains(text(), '对讲设置')]", "点击对讲设置")
        click(driver, By.XPATH, "(//*[contains(text(), '网络')])[2]", "点击网络")
        res = get_switch_status(driver, By.XPATH, '//*[@id="cms_cms_enable"]', "CMS")
        click(driver, By.XPATH, '//*[@id="cms_cms_enable"]', "当前:{},点击CMS按钮".format(switch_status[res]))
        click(driver, By.XPATH, "(//*[contains(text(), '保存')])[2]", "保存,当前CMS状态:{}".format(switch_status[not res]))
        check_save_success(driver, "CMS开关切换成功")
        check_switch(driver, By.XPATH, '//*[@id="cms_cms_enable"]', not res,
                     "CMS开关按钮状态检查,预期{}".format(switch_status[not res]))

        logout_right(driver)
        driver.close()

    @allure.story("网络-云平台")
    @allure.title("云平台启用和关闭,测试设备:{ip}")
    def test_network_cloud(self, driver, ip, user, password):
        start_case(driver, ip)
        model = login_right(driver, user, password)
        if model not in model_network_cloud:
            allure.step("当前型号{},没有网络-云平台功能".format(model))
            return
        click(driver, By.XPATH, "//*[contains(text(), '对讲设置')]", "点击对讲设置")
        click(driver, By.XPATH, "(//*[contains(text(), '网络')])[2]", "点击网络")
        res = get_switch_status(driver, By.XPATH, '//*[@id="cloud_enable"]', "云服务")
        click(driver, By.XPATH, '//*[@id="cloud_enable"]', "当前:{},点击云服务按钮".format(switch_status[res]))
        click(driver, By.XPATH, "(//*[contains(text(), '保存')])[3]", "保存,当前云服务状态:{}".format(switch_status[not res]))
        check_save_success(driver, "云平台开关切换成功")
        check_switch(driver, By.XPATH, '//*[@id="cloud_enable"]', not res,
                     "云平台开关按钮状态检查,预期{}".format(switch_status[not res]))

        logout_right(driver)
        driver.close()
