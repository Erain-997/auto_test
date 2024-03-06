import time


def check_box_status(driver, by, arg):
    element = driver.find_element(by, arg)
    return element.is_selected()


def check_element_true(driver, by, arg):
    element = driver.find_element(by, arg)
    assert element == True, "测试失败"


def click(driver, by, arg):
    element = driver.find_element(by, arg)
    if element:
        element.click()
    time.sleep(0.5)


def send(driver, by, path, arg):
    element = driver.find_element(by, path)
    element.send_keys(arg)
    time.sleep(0.5)
