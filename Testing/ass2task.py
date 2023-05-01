import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')

driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S-1526674172%3A1679724165402277&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ifkv=AQMjQ7SDkn6Wr41jLWLk6mjBfk22I-OjnPWgdBE-px9C7SPs-h9a-CQFoiiWR12y7WmWpb8xvtHNYw&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(7)
email_input = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
email_input.send_keys("200103126@stu.sdu.edu.kz")
next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(7)
password = driver.find_element(By.NAME,'Passwd')
password.send_keys("nuraina2003")
time.sleep(4)
go = driver.find_element(By.CSS_SELECTOR, '#passwordNext > div > button > span').click()
time.sleep(10)

test1 = driver.find_element(By.XPATH,'//*[@id=":5"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz[1]/c-wiz/div/c-wiz[4]')

test2 = driver.find_element(By.XPATH, '//*[@id=":5"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz[1]/c-wiz/div/c-wiz[5]')

actions = ActionChains(driver)
ActionChains(driver).drag_and_drop(test1, test2).perform()

time.sleep(5)

test = driver.find_element(By.XPATH, '//*[@id=":5"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz[1]/c-wiz/div/c-wiz[5]')
test3 = driver.find_element(By.XPATH, '//*[@id=":7h"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz/div/div/div/div/div[4]')
drive = driver.find_element(By.XPATH, '//*[@id="nt:Dr:label"]/div/span')

actions.double_click(test)
ActionChains(driver).drag_and_drop(test3, drive).perform()
time.sleep(5)


driver.close()