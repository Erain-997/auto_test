from airtest.core.api import snapshot

from api.app.app_assert import check_app_with_png
from api.app.app_tools import connect_devices_ip
from test.common import login_right, logout_right
from test.start import *


@allure.feature("常规设置-网络")
@allure.description("基础设置")
@pytest.mark.parametrize("ip, user, password", start())
class TestGeneral:
    @allure.story("休眠时间")
    def test_sleep(self, driver, ip, user, password):
        start_case(driver, ip)
        model = login_right(driver, user, password)
        click(driver, By.XPATH, '//li[2]/span', "点击常规设置->基础设置")
        click(driver, By.XPATH, "(//*[contains(text(), '1 分')])[1]", "点击显示-休眠时间")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), '15 秒')]", "检查下拉框元素-15秒")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), '30 秒')]", "检查下拉框元素-30秒")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), '1 分')]", "检查下拉框元素-1分")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), '2 分')]", "检查下拉框元素-2分")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), '5 分')]", "检查下拉框元素-5分")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), '10 分')]", "检查下拉框元素-10分")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), '30 分')]", "检查下拉框元素-30分")
        click(driver, By.XPATH, "(//*[contains(text(), '2 分')])[1]", "点击切换成2分")
        click(driver, By.XPATH, "(//*[contains(text(), '保存')])[2]", "点击显示-休眠时间-保存")
        # todo check 设备端

        click(driver, By.XPATH, "(//*[contains(text(), '2 分')])[1]", "点击切换成2分")
        click(driver, By.XPATH, "(//*[contains(text(), '1 分')])[1]", "点击显示-休眠时间")
        logout_right(driver)
        driver.close()

    @allure.story("基础设置")
    def test_device_language(self, driver, ip, user, password):
        start_case(driver, ip)
        model = login_right(driver, user, password)
        click(driver, By.XPATH, '//li[2]/span', "点击常规设置->基础设置")
        eee = click(driver, By.XPATH, "(//*[contains(text(), '简体中文')])[2]", "点击语言-简体中文")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), '繁體中文')]", "检查下拉框元素-繁體中文")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), 'עִברִית')]", "检查下拉框元素-עִברִית")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), 'Deutsch')]", "检查下拉框元素-Deutsch")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), 'Español')]", "检查下拉框元素-Español")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), 'Türkçe')]", "检查下拉框元素-Türkçe")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), 'Tiếng Việt')]", "检查下拉框元素-Tiếng Việt")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), 'Nederlands')]", "检查下拉框元素-Nederlands")
        check_element_exist(driver, By.XPATH, "//*[contains(text(), 'Português')]", "检查下拉框元素-Português")

        click(driver, By.XPATH, "//*[contains(text(), 'English')]", "点击切换成English")
        click(driver, By.XPATH, "(//*[contains(text(), '保存')])[2]", "点击语言-保存")
        # 容错， 等待生效
        time.sleep(2)

        name = "检查设备语言为英语"
        report_dir, poco = connect_devices_ip(name, ip)
        result = poco(text="Call").exists()
        snapshot(filename=report_dir + "/{}.png".format(name), quality=99)
        check_app_with_png(open(report_dir + "/{}.png".format(name), "rb").read(), report_dir, name, result)

        click(driver, By.XPATH, "//*[contains(text(), 'English')]", "点击语言-English")
        click(driver, By.XPATH, "(//*[contains(text(), '简体中文')])[2]", "点击切换成简体中文")
        click(driver, By.XPATH, "(//*[contains(text(), '保存')])[2]", "点击语言-保存")
        logout_right(driver)
        driver.close()
