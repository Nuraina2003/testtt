from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get('https://web.whatsapp.com/')
time.sleep(4)

maga = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div').click()
time.sleep(10)

maga1 = driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
time.sleep(4)

maga1.send_keys("Ulbolsyn")
maga1.send_keys(Keys.ENTER)
time.sleep(5)


maga1 = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
time.sleep(4)

maga1.send_keys("Hello")
maga1.send_keys(Keys.ENTER)
time.sleep(5)
