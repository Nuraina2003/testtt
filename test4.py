from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get('https://krisha.kz/')
open = driver.find_element(By.XPATH, '//*[@id="id-678356394"]').click()
time.sleep(5)
print(driver.current_window_handle)
handles = driver.window_handles

for handle in handles:
 driver.switch_to.window(handle)
 print(driver.title)
 if driver.title != "Продажа 1-комнатной квартиры - №678356394:Бурундайская — Северное кольцо, Алматы, Жетысуский р-н — за11500000 — Крыша":
    driver.close()