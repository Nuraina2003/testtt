
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Testing.db_test import data

driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get('https://www.facebook.com/')
@pytest.mark.parametrize("id, username, password", data)
def test_addition(id, username, password):
    name = driver.find_element(By.ID, 'email').send_keys(username)
    password_username = driver.find_element(By.ID, 'pass').send_keys(password)
    button = driver.find_element(By.NAME, 'login').click()
    time.sleep(4)