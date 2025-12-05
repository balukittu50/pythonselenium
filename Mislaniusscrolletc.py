import time

from selenium import webdriver

# to Run in Headlessmode
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("headless")
chromeoptions.add_argument("--ignore-certificate-errors")  # to ignore ssl certifications

driver = webdriver.Chrome(options=chromeoptions)
#driver = webdriver.Chrome(options=chromeoptions)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0,500);")  # executing java script for scrolling
time.sleep(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("down.png")  # screen shot
