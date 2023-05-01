from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get('https://the-internet.herokuapp.com/dynamic_controls')
time.sleep(5)
remove_button = driver.find_element(By.XPATH,'//*[@id="checkbox-example"]/button').click()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
Add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button'))).click()
time.sleep(5)
driver.close()

