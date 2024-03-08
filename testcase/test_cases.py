from service.test_start import server
from testcase.login.login import *


# 用例集合
class TestCases(server):
    # @allure.title("登录行为测试")
    # @pytest.mark.parametrize("driver", [start], indirect=True)  # 使用间接参数化，让 pytest 调用 webdriver fixture
    # @pytest.mark.parametrize("driver,user,password", [start])
    # @pytest.fixture检查勾选框
    @allure.title("登录行为测试")
    def test_cases(self):
        driver, user, password = self.start()
        # 测试用例1
        login_test(driver)
        # 测试用例2
        # login(driver, user, password)
        # input()

    def test_1(self):
        print(1)
        assert 1 == 1
