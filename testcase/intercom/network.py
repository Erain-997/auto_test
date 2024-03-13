from api.web import *
from api.web.assert_tools import *

from testcase import *

# todo
@allure.step("网络设置")
def network_dhcp(driver):
    click(driver, By.XPATH, '//*[@id="root"]//li[1]//span[2]', "点击收起常规设置")
    click(driver, By.XPATH, '//*[@id="root"]//li[2]//span[2]', "点击安防管理")
    click(driver, By.XPATH, "(//*[contains(text(), '网络')])[2]", "点击网络")
    res = get_switch_status(driver, By.XPATH, '//*[@id="network_dhcp"]',"dhcp")
    click(driver, By.XPATH, '//*[@id="network_dhcp"]', "点击dhcp按钮")
    res = get_switch_status(driver, By.XPATH, '//*[@id="network_dhcp"]',"dhcp")
    # todo 没加保存, 保存后丢失目标


@allure.step("网络-云平台")
def network_cloud(driver):
    click(driver, By.XPATH, '//*[@id="root"]//li[2]//span[2]', "点击安防管理")
    click(driver, By.XPATH, "(//*[contains(text(), '网络')])[2]", "点击网络")
    res = get_switch_status(driver, By.XPATH, '//*[@id="cloud_enable"]',"云服务")
    click(driver, By.XPATH, '//*[@id="cloud_enable"]', "当前:{},点击云服务按钮".format(switch_status[res]))
    time.sleep(0.5)
    click(driver, By.XPATH, "(//*[contains(text(), '保存')])[3]", "保存,当前云服务状态:".format(switch_status[not res]))
    time.sleep(2)
    check_switch(driver, By.XPATH, '//*[@id="network_dhcp"]', not res,
                 "云平台开关按钮状态检查,预期{}".format(switch_status[not res]))
