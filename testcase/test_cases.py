from service.test_start import Server
from testcase.general.information import *
from testcase.login.login import *


# 用例集合
class TestCases(Server):
    # @allure.title("登录行为测试")
    # @pytest.mark.parametrize("driver", [start], indirect=True)  # 使用间接参数化，让 pytest 调用 webdriver fixture
    # @pytest.mark.parametrize("driver,user,password", [start])
    # @pytest.fixture检查勾选框

    @allure.title("登录相关测试")
    def test_cases(self):
        driver, user, password = self.start()
        # 测试用例1
        login_test(driver)
        # 测试用例2
        login_ok(driver, user, password)

    @allure.title("升级系统")
    def test_information(self):
        driver, user, password = self.start()
        login_ok(driver, user, password)
        update_system(driver)
        # input()

