from api.web import *
from api.web.assert_tools import *
from test import *
from test.start import *


@allure.feature("对讲设置-呼叫")
@pytest.mark.parametrize("url, user, password", start())
class TestCall:
    @allure.story("高级-聋哑模式")
    @allure.description("web端验证聋哑模式的开启/关闭状态")
    def test_deaf(self, driver, url, user, password):
        start_case(driver, url)
        model = login_right(driver, user, password)
        # if model not in model_network_cloud:
        #     allure.step("当前型号{},没有网络-云平台功能".format(model))
        #     return
        click(driver, By.XPATH, "//*[contains(text(), '对讲设置')]", "点击对讲设置")
        click(driver, By.XPATH, "//*[contains(text(), '呼叫')]", "点击呼叫")
        res = get_switch_status(driver, By.XPATH, '//*[@id="advanced_deaf"]', "聋哑模式")
        click(driver, By.XPATH, '//*[@id="advanced_deaf"]', "当前:{},点击聋哑模式按钮".format(switch_status[res]))
        click(driver, By.XPATH, "(//*[contains(text(), '保存')])[2]", "保存,当前聋哑模式开关状态:{}".format(switch_status[not res]))
        check_save_success(driver, "聋哑模式切换成功")
        check_switch(driver, By.XPATH, '//*[@id="advanced_deaf"]', not res,
                     "聋哑模式开关按钮状态检查,预期{}".format(switch_status[not res]))

        logout_right(driver)
        driver.close()

    @allure.story("高级-摄像头")
    @allure.description("web端验证摄像头的开启/关闭状态")
    def test_camera(self, driver, url, user, password):
        start_case(driver, url)
        model = login_right(driver, user, password)
        # if model not in model_network_cloud:
        #     allure.step("当前型号{},没有网络-云平台功能".format(model))
        #     return
        click(driver, By.XPATH, "//*[contains(text(), '对讲设置')]", "点击对讲设置")
        click(driver, By.XPATH, "//*[contains(text(), '呼叫')]", "点击呼叫")
        res = get_switch_status(driver, By.XPATH, '//*[@id="advanced_camera"]', "摄像头")
        click(driver, By.XPATH, '//*[@id="advanced_camera"]', "当前:{},点击摄像头按钮".format(switch_status[res]))
        click(driver, By.XPATH, "(//*[contains(text(), '保存')])[2]", "保存,当前摄像头开关状态:{}".format(switch_status[not res]))
        check_save_success(driver, "摄像头切换成功")
        check_switch(driver, By.XPATH, '//*[@id="advanced_camera"]', not res,
                     "摄像头开关按钮状态检查,预期{}".format(switch_status[not res]))

        logout_right(driver)
        driver.close()
