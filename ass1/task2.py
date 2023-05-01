from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get('https://www.facebook.com')
time.sleep(5)
email = driver.find_element(By.NAME,'email')
email.send_keys('87753120720')
time.sleep(10)
passwd = driver.find_element(By.NAME,'pass')
passwd.send_keys('nuraina2003')
time.sleep(10)
login = driver.find_element(By.NAME,'login').click()

time.sleep(5)
driver.close()