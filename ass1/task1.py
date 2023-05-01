from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get('https://www.google.com/')
search = driver.find_element(By.CLASS_NAME, 'gLFyf')
search.send_keys("Selenium")
search.send_keys(Keys.ENTER)
result = driver.find_element(By.XPATH,'//*[@id="rso"]').click()
driver.close()