import allure

# 校验元素是否存在
import pytest


def check_app_with_png(img, text, case_name, status):
    with allure.step(case_name):
        allure.attach(img, name=text, attachment_type=allure.attachment_type.PNG)
        if not status:
            pytest.fail(text)
