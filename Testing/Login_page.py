from selenium import webdriver
import time
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.button_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,'Да')))
        self.search_input = WebDriverWait(self.driver, 10 ).until(EC.presence_of_element_located((By.NAME , 'q')))
    def enter_search(self, search):
        self.search_input.clear()
        self.search_input.send_keys('Iphone')
    def click_button(self):
        self.button_input.click()

def test_home():
    driver = webdriver.Chrome()
    driver.get("https://www.sulpak.kz/")
    home_page = HomePage(driver)
    home_page.click_button()
    home_page.enter_search('Iphone')
    assert driver.title != 'Home'
    driver.quit()