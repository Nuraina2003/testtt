import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')

driver.get('https://drive.google.com/drive/')
time.sleep(7)
open = driver.find_element(By.XPATH,'//*[@id="hero-cta-wrapper"]/a[2]').click()
time.sleep(7)
search_bar = driver.find_element(By.XPATH,'//*[@id=\"identifierId\"]')
time.sleep(5)
search_bar.send_keys("200103126@stu.sdu.edu.kz")
search_bar.send_keys(Keys.ENTER)
next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(7)
password = driver.find_element(By.NAME,'Passwd')
password.send_keys("nuraina2003")
time.sleep(4)
go = driver.find_element(By.CSS_SELECTOR, '#passwordNext > div > button > span').click()
time.sleep(20)
driver.close()