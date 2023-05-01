from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get('https://kolesa.kz/')
ads = driver.find_element(By.XPATH, '//*[@id="minPageHotBlock"]').click()
time.sleep(5)
print(driver.current_window_handle)
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title != "Tiggo 8 Pro Max":
        time.sleep(5)
        driver.close()
