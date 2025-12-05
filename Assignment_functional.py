import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actuallist = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
# it wait max time 5 sec if it find with in that it will procedeu to next steps
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
assert len(results) > 0
for result in results:
    actuallist.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()
assert expected_list == actuallist
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
tot = 0
for price in prices:
    tot = tot + int(price.text)
print(tot)
Totalamount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert tot == Totalamount
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# Explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))
# time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
discontamt = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
assert Totalamount > discontamt
