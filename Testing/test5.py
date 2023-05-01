from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



@pytest.fixture
def browser():
    driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
    yield driver
def  test_search_google(browser):
    browser.get('https://www.google.com')
    search_box = browser.find_element(By.CLASS_NAME, 'q')
    # Your existing code here to interact with the website
    # Add assertions to verify that the product was successfully removed from the cart
