from selenium import webdriver
import time
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.button_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,'Да')))
        self.profile_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,'Личный кабинет')))
        self.signin_input = WebDriverWait(self.driver, 10 ).until(EC.presence_of_element_located((By.LINK_TEXT , 'Войти с паролем')))

    def click_button(self):
        self.button_input.click()

    def click_profile(self):
        self.profile_input.click()

    def enter_sign_in(self):
        self.signin_input.click()

def test_profile():
    driver = webdriver.Chrome()
    driver.get("https://www.sulpak.kz/")
    profile_page = ProfilePage(driver)
    profile_page.click_signin()
    profile_page.click_profile()
    profile_page.click_button()
    assert driver.title != 'Profile'
    driver.quit()


