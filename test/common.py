# from service.test_start import Server
# from test.general.information import *
# from test.intercom.network import *
# from test.test_login.test_login import *
#
#
# # 用例集合
# # todo 标签美化
# # todo 正则优化
# class TestCases(Server):
# @allure.title("登录行为测试")
# @pytest.mark.parametrize("driver", [start], indirect=True)  # 使用间接参数化，让 pytest 调用 webdriver fixture
# @pytest.mark.parametrize("driver,user,password", [start])
# @pytest.fixture检查勾选框

# # @pytest.mark.skip
# @allure.title("登录相关测试")
# def test_login(self):
#     driver, user, password = self.start()
#     # 登录界面语言测试
#     login_language(driver)
#     # 登录界面输入框测试
#     login_test(driver)
#     # 成功登录-不记住
#     login_ok(driver, user, password)
#     # 记住登录
#     login_out_check_remember(driver)
#     # 退出校验,再记住登录
#     login_out_check_not_remember(driver, user, password)
#
# # @pytest.mark.skip
# @allure.title("切换语言")
# def test_language(self):
#     driver, user, password = self.start()
#     login_ok(driver, user, password)
#     change_language(driver)
#     # time.sleep(10000)
#     # input()
#
# # @pytest.mark.skip
# @allure.title("网络测试")
# def test_intercom(self):
#     driver, user, password = self.start()
#     model = login_ok(driver, user, password)
#     # network_dhcp(driver)
#     if model in model_network_cloud:
#         network_cloud(driver)
#
# @pytest.mark.skip
# @allure.title("升级系统")
# def test_update_system(self):
#     driver, user, password = self.start()
#     login_ok(driver, user, password)
#     update_system(driver)
#     # input()



from api.web import *
from api.web.assert_tools import *
# 准备各种符号和数据组合的测试数据
from test.start import *
from test import box_status
from test.test_login import *


def login_right(driver, user, password, remember=True) -> str:
    # todo 正则优化
    clear(driver, By.ID, "login_username")
    send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
    clear(driver, By.ID, "login_password")
    send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
    res = get_box_status(driver, By.XPATH, '//*[@id="login_remember"]', "记住我")
    if remember and not res:
        click(driver, By.XPATH, '//*[@id="login_remember"]', "点击记住我勾选框")
        check_box(driver, By.XPATH, '//*[@id="login_remember"]', not res,
                  "记住我勾选框状态检查,预期{}".format(box_status[not res]))
    click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")
    # check_element_exist(driver, By.XPATH, "//*[contains(text(), '设备')]", True, "校验登录-预期登录成功")
    model = get_model(driver, By.XPATH,
                      "//div[@class='ant-statistic-title' and text()='型号']/following-sibling::div/span[@class='ant-statistic-content-value']")
    return model
