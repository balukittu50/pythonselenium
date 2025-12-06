import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = "kittu"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
assert name in alert.text
alert.accept()
#alert.dismiss()



