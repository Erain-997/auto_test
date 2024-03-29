from airtest.core.api import snapshot
from api.app.app_assert import check_app_with_png
from api.app.app_tools import connect_devices_ip
from api.web.func import click, get_attribute_text
from test.common import login_right
from test.start import *


# @allure.feature("常规设置-信息")
# @allure.description("设备信息")
# @pytest.mark.parametrize("ip, user, password", start())
# class TestGeneral:
#     @allure.story("默认Model显示")
#     @allure.title("[web]查看设备信息")
#     @allure.feature("人工确认截图内容")
#     def test_model(self, driver, ip, user, password):
#         start_case(driver, ip)
#         model = login_right(driver, user, password)
#         with allure.step("检查型号名称,预期:{}".format("Android Door Station")):
#             try:
#                 assert model == "Android Door Station"
#                 allure.attach(driver.get_screenshot_as_png(), name="设备信息界面", attachment_type=allure.attachment_type.PNG)
#             except AssertionError as e:
#                 with allure.step("文本内容校验失败,预期:{},实际{}".format("Android Door Station", model)):
#                     allure_attach(driver, "", "文本内容校验失败,预期:{},实际{}.".format("Android Door Station", model) + str(e))
#                     pytest.fail("请确认门口机型号")
#
#     # @allure.story("special修改Model，查看Information-Model")
#     # @allure.title("[web]查看设备信息")
#     # # todo bug
#     # def test_change_model(self, driver, ip, user, password):
#     #     start_case(driver, ip)
#     #     model = login_right(driver, "special", "dnake2005")
#     #     with allure.step("检查型号名称,预期:{}".format("Android Door Station")):
#     #         try:
#     #             assert model == "Android Door Station"
#     #             allure.attach(driver.get_screenshot_as_png(), name="设备信息界面", attachment_type=allure.attachment_type.PNG)
#     #         except AssertionError as e:
#     #             with allure.step("文本内容校验失败,预期:{},实际{}".format("Android Door Station", model)):
#     #                 allure_attach(driver, "", "文本内容校验失败,预期:{},实际{}.".format("Android Door Station", model) + str(e))
#     #                 pytest.fail("请确认门口机型号")
#     #
#     # click(driver, By.XPATH, "//*[contains(text(), '高级设置')]", "点击高级设置")
#     # click(driver, By.XPATH, "//*[contains(text(), 'Android Door Station')]", "点击Android Door Station")
#     # click(driver, By.XPATH, "//*[contains(text(), 'S615')]", "点击S615")
#     # click(driver, By.XPATH, "//*[contains(text(), '保存')]", "点击保存")
#     #
#     # check_save_success(driver, "型号保存成功")
#     # click(driver, By.XPATH, "//*[contains(text(), '信息')]", "点击信息")
#
#     #
#     # @allure.step("升级系统")
#     # def update_system(driver):
#     #     click(driver, By.XPATH, '//li[5]/span', "点击常规设置->系统")
#     #
#     #
#     # @allure.step("设备信息校验")
#     # def check_information(driver):
#     #     res = get_attribute_text(driver, By.XPATH, '//*[@id="root"]//div[1]/div[1]/div[2]/div[1]/div')
#     #     print(datetime.now(), ": ", res, "-----------")
#
#     @allure.story("about-systerm显示")
#     @allure.title("[web]查看设备系统信息")
#     # @allure.label("人工确认截图内容")
#     # @pytest.mark.DoubleCheck
#     def test_model(self, driver, ip, user, password):
#         start_case(driver, ip)
#         model = login_right(driver, user, password)
#
#         name = "设备系统信息截图"
#         report_dir, poco = connect_devices_ip(name, ip)
#         time.sleep(1)
#         snapshot(filename=report_dir + "/{}.png".format(name), quality=99)
#         check_app_with_png(open(report_dir + "/{}.png".format(name), "rb").read(), report_dir, name, True)
#
#         # with allure.step("检查型号名称,预期:{}".format("Android Door Station")):
#         #     try:
#         #         assert model == "Android Door Station"
#         #         allure.attach(driver.get_screenshot_as_png(), name="设备信息界面", attachment_type=allure.attachment_type.PNG)
#         #     except AssertionError as e:
#         #         with allure.step("文本内容校验失败,预期:{},实际{}".format("Android Door Station", model)):
#         #             allure_attach(driver, "", "文本内容校验失败,预期:{},实际{}.".format("Android Door Station", model) + str(e))
#         #             pytest.fail("请确认门口机型号")
#

class TestCase01():
    @allure.severity(allure.severity_level.BLOCKER)
    def test_case_01(self):
        with allure.step("Step 1"):
            assert False, "This test case is blocked."

    @pytest.mark.xfail(reason="测试用例执行结果未知")
    def test_case_02(self):
        time.sleep(1)
        print("case02$$$$$$$$$$$$$$$$$$$$$")
        assert 3 == 3

    @allure.tag("用例集合")
    @pytest.mark.web
    def test_case_03(self):
        time.sleep(1)
        print("case03$$$$$$$$$$$$$$$$$$$$$")
        assert "is" in "is_you"

    @pytest.mark.BBB
    def test_case_04(self):
        time.sleep(1)
        print("case04$$$$$$$$$$$$$$$$$$$$$")
        assert 5 < 10

    @pytest.mark.AAA
    @pytest.mark.xfail
    def test_case_05(self):
        time.sleep(1)
        print("case05$$$$$$$$$$$$$$$$$$$$$")
        assert 222 == 333

    def test_case_06(self):
        time.sleep(1)
        print("case06$$$$$$$$$$$$$$$$$$$$$")
        assert 444 > 666


class TestCase02():
    @pytest.mark.skip
    def test_case_07(self):
        time.sleep(1)
        print("case07$$$$$$$$$$$$$$$$$$$$$")
        assert 10 / 2 == 5.0

    @pytest.mark.xfail
    def test_case_08(self):
        time.sleep(1)
        print("case08$$$$$$$$$$$$$$$$$$$$$")
        assert "num" in "num_list"

    @pytest.mark.flaky
    def test_case_09(self):
        time.sleep(1)
        print("case08$$$$$$$$$$$$$$$$$$$$$")
        assert "num1" in "num_list"


class TestCase03():
    @allure.severity(allure.severity_level.BLOCKER)
    def test_BLOCKER_testcase(self):
        with allure.step("Step 1"):
            assert True, "This test case is BLOCKER."

    @allure.severity(allure.severity_level.CRITICAL)
    def test_critical_testcase(self):
        with allure.step("Step 1"):
            assert True, "This test case is CRITICAL."

    @allure.severity(allure.severity_level.NORMAL)
    def test_NORMAL_testcase(self):
        with allure.step("Step 1"):
            assert True, "This test case is NORMAL."

    @allure.severity(allure.severity_level.MINOR)
    def test_MINOR_testcase(self):
        with allure.step("Step 1"):
            assert True, "This test case is MINOR."

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_TRIVIAL_testcase(self):
        with allure.step("Step 1"):
            assert True, "This test case is TRIVIAL."

    # @allure.dynamic.story('未知的测试用例')
    # def test_unknown(self):
    #     allure.dynamic.description('测试用例执行结果未知')






