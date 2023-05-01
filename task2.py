from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/Users/Привет/Downloads/chromedriver_win32/webdriver.exe')
driver.get("https://demo.automationtesting.in/Alerts.html")

alert_button = driver.find_element(By.XPATH, '//*[@id="OKTab"]').click()
time.sleep(5)
alt = driver.switch_to.alert
alt.accept()

# # Task 2: Alert with Ok & Cancel
alert_button = driver.find_element(By.LINK_TEXT, 'Alert with OK & Cancel').click()
ok_cancel = driver.find_element(By.XPATH, '//*[@id="CancelTab"]').click()

alt = driver.switch_to.alert
alt.dismiss()
time.sleep(4)

ok_cancel = driver.find_element(By.XPATH, '//*[@id="CancelTab"]').click()

alt = driver.switch_to.alert
alt.accept()
time.sleep(3)

#Task3
alert_button = driver.find_element(By.LINK_TEXT, 'Alert with Textbox').click()
ok_cancel = driver.find_element(By.XPATH, '//*[@id="Textbox"]').click()
alt = driver.switch_to.alert
alt.send_keys("Nuraina")
alt.accept()

driver.quit()

