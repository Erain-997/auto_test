from service.test_start import Server
from testcase.general.haha import *
from testcase.general.information import *
from testcase.intercom.network import *
from testcase.login.login import *


# 用例集合
# todo 标签美化
# todo 正则优化
class TestCases(Server):
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

    @allure.title("测试用的")
    def test_aaaa(self):
        aaa()
        bbb()
        ccc()




