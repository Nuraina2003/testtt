from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get('https://www.calculator.net/')
driver.implicitly_wait(5)
n1 = driver.find_element(By.XPATH, '//span[@onclick="r(1)"]').click()
plus = driver.find_element(By.XPATH, '//span[@onclick="r(\'+\')"]').click()
n2 = driver.find_element(By.XPATH, '//span[@onclick="r(2)"]').click()
result_field = driver.find_element(By.XPATH, "//div[@id='sciOutPut']")
actions = ActionChains(driver)
actions.click(n1)
actions.click(plus)
actions.click(n2)
result = result_field.text
print("Result is: " + result)
driver.implicitly_wait(3)
C = driver.find_element(By.CSS_SELECTOR, '#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(5) > span:nth-child(3)').click()
actions = ActionChains(driver)
actions.click(C)


n5 = driver.find_element(By.XPATH,'//span[@onclick="r(5)"]').click()
minus = driver.find_element(By.XPATH, '//span[@onclick="r(\'-\')"]').click()
n3 = driver.find_element(By.XPATH, '//span[@onclick="r(3)"]').click()
result_field = driver.find_element(By.XPATH, "//div[@id='sciOutPut']")
actions = ActionChains(driver)
actions.click(n5)
actions.click(minus)
actions.click(n3)
result = result_field.text
print("Result is: " + result)

driver.implicitly_wait(3)
C = driver.find_element(By.CSS_SELECTOR, '#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(5) > span:nth-child(3)').click()
actions = ActionChains(driver)
actions.click(C)

n5 = driver.find_element(By.XPATH,'//span[@onclick="r(5)"]').click()
mult = driver.find_element(By.XPATH, '//span[@onclick="r(\'*\')"]').click()
n3 = driver.find_element(By.XPATH, '//span[@onclick="r(3)"]').click()
result_field = driver.find_element(By.XPATH, "//div[@id='sciOutPut']")
actions = ActionChains(driver)
actions.click(n5)
actions.click(mult)
actions.click(n3)
result = result_field.text
print("Result is: " + result)
driver.implicitly_wait(3)
C = driver.find_element(By.CSS_SELECTOR, '#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(5) > span:nth-child(3)').click()
actions = ActionChains(driver)
actions.click(C)


n5 = driver.find_element(By.XPATH,'//span[@onclick="r(5)"]').click()
div = driver.find_element(By.XPATH, '//span[@onclick="r(\'/\')"]').click()
n3 = driver.find_element(By.XPATH, '//span[@onclick="r(3)"]').click()
result_field = driver.find_element(By.XPATH, "//div[@id='sciOutPut']")
actions = ActionChains(driver)
actions.click(n5)
actions.click(div)
actions.click(n3)
result = result_field.text
print("Result is: " + result)
driver.implicitly_wait(5)
C = driver.find_element(By.CSS_SELECTOR, '#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(5) > span:nth-child(3)').click()
actions = ActionChains(driver)
actions.click(C)

driver.quit()
