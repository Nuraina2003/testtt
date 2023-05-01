import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.sulpak.kz/')

def test_add_to_cart(setup):
    wait = WebDriverWait(setup, 10)
    nurai = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popup_city_default"]/div[1]/div/div/div/div[3]/a[2]')))
    nurai.click()

    search = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="evinent-search"]')))
    search.send_keys("Iphone")
    search.send_keys(Keys.ENTER)

    product = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="products"]/div[1]/div/div/div[1]/a/div')))
    product.click()

    color = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rewiew-tab-container"]/div[1]/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/a[1]')))
    color.click()

    storage = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rewiew-tab-container"]/div[1]/div/div/div[3]/div[2]/div[1]/div[2]/div[2]/a[3]')))
    storage.click()

    basket = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Купить')))
    basket.click()

    basket = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Перейти в корзину')))
    basket.click()

    remove = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cart__products"]/div[1]/div/div[1]/div[5]/a')))
    remove.click()

    remove1 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Удалить')))
    remove1.click()


