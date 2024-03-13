import allure
import pytest


@allure.title("AAA")
def aaa():
    name = "aaa"
    with allure.step(name + "111"):
        pass
    with allure.step(name + "222"):
        pass
    with allure.step(name + "333"):
        pass


@allure.step("BBB")
def bbb():
    name = "bbb"
    with allure.step(name + "111"):
        try:
            assert 2 + 2 == 5
        except AssertionError:
            allure.attach("1111", name="xpath路径", attachment_type=allure.attachment_type.TEXT)
            # pytest.fail("我失败了")
    with allure.step(name + "222"):
        pass

    with allure.step(name + "333"):
        pass


@allure.step("CCC")
def ccc():
    name = "ccc"
    with allure.step(name + "111"):
        pass
    with allure.step(name + "222"):
        pass
    with allure.step(name + "333"):
        pass
