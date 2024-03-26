from api.tools import *

# 准备各种符号和数据组合的测试数据
from test.start import *
from test import box_status
from test.login import *
from test.common import login_right, logout_right

test_data = [
    (generate_data_all(6), generate_data_all(6), False),  # 随机整合数据
    ("user1", "wrongpass", False),  # 错误的密码
    ("wronguser", "pass1", False),  # 错误的用户名
    # ("user1", "", False),  # 空密码
    # ("", "pass1", False),  # 空用户名
    # ("User1", "pass1", False),  # 用户名大小写敏感
    # ("user1", "Pass1", False),  # 密码大小写敏感
    # ("user1", "pass11", False),  # 密码太长
    # ("user1", "pa", False),  # 密码太短
    # ("@user1", "pass1", False),  # 用户名包含特殊字符
    # ("user1", "!pass1", False),  # 密码包含特殊字符
    # ... 可以继续添加更多的测试数据
]


@allure.feature("登录模块")
@pytest.mark.parametrize("ip, user, password", start())
class TestLogin:
    # @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("正确登录-默认勾选记住")
    def test_login_right(self, driver, ip, user, password):
        # telnet_reset_login(ip, 9900, user, password)
        start_case(driver, ip)
        login_right(driver, user, password)

        # 恢复环境
        logout_right(driver)
        driver.close()

    @allure.story("错误密码登录")
    def test_login_wrong(self, driver, ip, user, password):
        start_case(driver, ip)
        click(driver, By.XPATH, "//span[contains(@class, 'anticon-eye-invisible')]", "点击显示密码")
        for data in test_data:
            user, password = data[0], data[1]
            send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
            send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
            res = get_box_status(driver, By.XPATH, '//*[@id="login_remember"]', "记住我")
            click(driver, By.XPATH, '//*[@id="login_remember"]', "点击记住我勾选框")
            check_box(driver, By.XPATH, '//*[@id="login_remember"]', not res,
                      "记住我勾选框状态检查,预期{}".format(box_status[not res]))
            click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")
            check_text(driver, By.XPATH, '//*[@id="login_username"]', "")
            check_text(driver, By.XPATH, '//*[@id="login_password"]', "")

        # 恢复环境
        driver.close()

    @allure.story("退出登录-记住我")
    def test_login_out_check_remember(self, driver, ip, user, password):
        start_case(driver, ip)

        clear(driver, By.ID, "login_username")
        send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
        clear(driver, By.ID, "login_password")
        send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
        click(driver, By.XPATH, '//*[@id="login_remember"]', "勾选记住我勾选框")
        click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")
        click(driver, By.XPATH, '//*[@id="root"]/section/header/div/a', "点击你好")
        click(driver, By.XPATH, '/html/body/div[2]/div/div/ul/li/span', "退出登录")
        time.sleep(1)
        check_box(driver, By.XPATH, '//*[@id="login_remember"]', True, "记住我勾选框状态检查,预期{}".format(box_status[True]))
        check_text_value(driver, By.XPATH, '//*[@id="login_username"]', user)
        click(driver, By.XPATH, "//span[contains(@class, 'anticon-eye-invisible')]", "点击显示密码")
        check_text_value(driver, By.XPATH, '//*[@id="login_password"]', password)

        # 恢复环境
        click(driver, By.XPATH, '//*[@id="login_remember"]', "取消记住我勾选框")
        click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")
        logout_right(driver)
        driver.close()

    @allure.story("退出登录-不记住我")
    def test_login_out_check_not_remember(self, driver, ip, user, password):
        start_case(driver, ip)

        clear(driver, By.ID, "login_username")
        send_text(driver, By.ID, "login_username", user, "输入用户名: " + user)
        clear(driver, By.ID, "login_password")
        send_text(driver, By.ID, "login_password", password, "输入密码: " + password)
        click(driver, By.XPATH, "//*[contains(text(), '登 录')]", "点击登录")
        click(driver, By.XPATH, '//*[@id="root"]/section/header/div/a', "点击你好")
        click(driver, By.XPATH, '/html/body/div[2]/div/div/ul/li/span', "退出登录")
        time.sleep(1)
        check_box(driver, By.XPATH, '//*[@id="login_remember"]', False, "记住我勾选框状态检查,预期{}".format(box_status[False]))
        check_text(driver, By.ID, "login_username", "")

        driver.close()

    @allure.story("登录界面-切换语言")
    def test_login_language(self, driver, ip, user, password):
        start_case(driver, ip)
        click(driver, By.XPATH, "//*[contains(text(), '简体中文')]", "登录界面点击语言")
        click(driver, By.XPATH, "//*[contains(text(), 'English')]", "切换成English")
        check_text(driver, By.XPATH, '//*[@id="login"]/div[4]//div/button/span', 'Sign in')
        click(driver, By.XPATH, "//*[contains(text(), 'English')]", "登录界面点击语言")
        click(driver, By.XPATH, "//*[contains(text(), '简体中文')]", "切换成中文")
        check_text(driver, By.XPATH, '//*[@id="login"]/div[4]//div/button/span', "登 录")

        # todo 新增用例, 登录后校验语言
        # logout_right(driver)
        driver.close()

    @allure.story("登录后-切换语言")
    def test_change_language(self, driver, ip, user, password):
        # 获取焦点
        # dropdown = driver.find_element(By.XPATH, '//*[@id="root"]/section/header//button/span[2]')
        # # 使用鼠标移动到下拉框元素，使其获得焦点
        # actions = ActionChains(driver)
        # actions.move_to_element(dropdown).perform()
        # 环境启动
        start_case(driver, ip)
        login_right(driver, user, password)
        # 定位下拉框元素
        click(driver, By.XPATH, '//*[@id="root"]/section/header//button/span[2]', "点击语言")
        click(driver, By.XPATH, '/html/body/div[2]//ul/li[1]/span', "切换成中文")
        check_text(driver, By.XPATH, '//*[@id="root"]//li[1]//span[2]', "常规设置")
        click(driver, By.XPATH, '//*[@id="root"]/section/header//button/span[2]', "点击语言")
        click(driver, By.XPATH, '/html/body/div[2]//ul/li[2]/span', "切换成英文")
        check_text(driver, By.XPATH, '//*[@id="root"]//li[1]//span[2]', "General")

        # 恢复环境
        click(driver, By.XPATH, '//*[@id="root"]/section/header//button/span[2]', "点击语言")
        click(driver, By.XPATH, '/html/body/div[2]//ul/li[1]/span', "切换成中文")
        logout_right(driver)
        driver.close()
