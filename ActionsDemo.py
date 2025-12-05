import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
actions = ActionChains(driver)
#actions.click_and_hold().perform()
# actions.context_click().perform()
# actions.double_click().perform()
actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(5)
