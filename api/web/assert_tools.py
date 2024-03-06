import allure
from allure_commons.types import AttachmentType

def check_box(driver, by, arg, states):
    with allure.step("检查勾选框"):
        element = driver.find_element(by, arg)
        assert element.is_selected() == states, "勾选失败"

    #     # 附加截图或其他文件作为结果记录
    # with allure.attach("Calculation Result", "text/plain") as attachment:
    #     attachment.add_file(states, file_name="result.txt", attachment_type=AttachmentType.TEXT)



def check_element_false(driver, by, arg):
    element = driver.find_element(by, arg)
    assert element == False, "测试失败"