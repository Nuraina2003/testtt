from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get('https://gate2home.com/English-Keyboard')
driver.implicitly_wait(4)
caps = driver.find_element(By.XPATH, '//*[@id="kb_bcaps"]').click()
A = driver.find_element(By.ID, 'kb_b26').click()
caps1 = driver.find_element(By.XPATH, '//*[@id="kb_bcaps"]').click()
u = driver.find_element(By.XPATH, '//*[@id="kb_b20"]').click()
t = driver.find_element(By.XPATH, '//*[@id="kb_b18"]').click()
o = driver.find_element(By.XPATH, '//*[@id="kb_b22"]').click()
m = driver.find_element(By.XPATH, '//*[@id="kb_b43"]').click()
a = driver.find_element(By.XPATH, '//*[@id="kb_b26"]').click()
t = driver.find_element(By.XPATH, '//*[@id="kb_b18"]').click()
i = driver.find_element(By.XPATH, '//*[@id="kb_b21"]').click()
o = driver.find_element(By.XPATH, '//*[@id="kb_b22"]').click()
n = driver.find_element(By.XPATH, '//*[@id="kb_b42"]').click()

#sp = driver.find_element(By.XPATH, '//*[@id="kb_bspace"]').click()
i = driver.find_element(By.XPATH, '//*[@id="kb_b21"]').click()
n = driver.find_element(By.XPATH, '//*[@id="kb_b42"]').click()
t = driver.find_element(By.XPATH, '//*[@id="kb_b18"]').click()
e = driver.find_element(By.XPATH, '//*[@id="kb_b16"]').click()
s = driver.find_element(By.XPATH, '//*[@id="kb_b27"]').click()
t = driver.find_element(By.XPATH, '//*[@id="kb_b18"]').click()
i = driver.find_element(By.XPATH, '//*[@id="kb_b21"]').click()
n = driver.find_element(By.XPATH, '//*[@id="kb_b42"]').click()
g = driver.find_element(By.XPATH, '//*[@id="kb_b30"]').click()
driver.implicitly_wait(5)
actions = ActionChains(driver)
actions.click(caps)
actions.click(A)
actions.click(caps1)
actions.click(u)
actions.click(t)
actions.click(o)
actions.click(m)
actions.click(a)
actions.click(t)
actions.click(i)
actions.click(o)
actions.click(n)


actions.click(e)
actions.click(s)
actions.click(g)




















