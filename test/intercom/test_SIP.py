from api.web import *
from api.web.assert_tools import *
from test.common import *
from test.start import *
from test import switch_status


@allure.feature("对讲设置-SIP")
@pytest.mark.parametrize("ip, user, password", start())
class TestSIP:
    @allure.story("SIP开关按钮")
    def test_SIP(self, driver, ip, user, password):
        start_case(driver, ip)
        model = login_right(driver, user, password)
        # if model not in model_network_cloud:
        #     allure.step("当前型号{},没有网络-云平台功能".format(model))
        #     return
        click(driver, By.XPATH, "//*[contains(text(), '对讲设置')]", "点击对讲设置")
        click(driver, By.XPATH, "(//*[contains(text(), 'SIP')])[2]", "点击SIP")
        res = get_switch_status(driver, By.XPATH, '//*[@id="voip_enable"]', "SIP")
        click(driver, By.XPATH, '//*[@id="voip_enable"]', "当前:{},点击SIP按钮".format(switch_status[res]))
        click(driver, By.XPATH, "(//*[contains(text(), '保存')])[1]", "保存,当前SIP状态:{}".format(switch_status[not res]))
        check_save_success(driver, "SIP开关切换成功")
        check_switch(driver, By.XPATH, '//*[@id="voip_enable"]', not res,
                     "SIP开关按钮状态检查,预期{}".format(switch_status[not res]))

        logout_right(driver)
        driver.close()
