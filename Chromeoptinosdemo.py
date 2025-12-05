import time

from selenium import webdriver

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--start-maximized")
# chromeoptions.add_argument("headless")
chromeoptions.add_argument("--ignore-certificate-errors")
chromeoptions.add_argument("--incognito")

driver = webdriver.Chrome(options=chromeoptions)
driver.get("https://google.com")
time.sleep(3)
print(driver.title)
