import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# if chrome driver is not detected then
# ser_obj=Service("Path of the driver downloaded")
# driver = webdriver.Chrome(ser_obj)

# Chrome driver service selenium -----Chromeversion 130 autmoatically detect driver version
driver = webdriver.Chrome()  # to Run on Chrome

# driver = webdriver.Firefox() #to Run on Firefox
# driver = webdriver.Edge() #to Run on edge

driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)
