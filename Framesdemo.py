import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.switch_to.frame("courses-iframe")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".lucide.lucide-x.h-4.w-4")))
driver.find_element(By.CSS_SELECTOR, ".lucide.lucide-x.h-4.w-4").click()
driver.find_element(By.LINK_TEXT, "JOIN NOW").click()
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h1").text)
