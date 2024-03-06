import pytest
import os
import shutil

# pytest --alluredir=reports
# allure serve /report
if __name__ == '__main__':
    dir_path = '/allure-results'
    if os.path.exists(dir_path):
        print(222222222)
        shutil.rmtree(dir_path)
    # os.mkdir(dir_path)

    pytest.main(['-s', '-v', '--alluredir=./allure-results', "testcase/"])

    # driver.implicitly_wait(100)
    # driver.close()
