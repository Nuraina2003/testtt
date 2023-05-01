from selenium import webdriver
#import pytest
#from selenium.webdriver import Keys
#from selenium.webdriver.common.by import By
driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get("https://sdu.edu.kz/")

import pytest
@pytest.mark.fast
def test_my_fast_test():
    sdu = 'sdu'
    assert 'sdu' in sdu
