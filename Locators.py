import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()  # to Run on Chrome
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# id,xpath,css,linktext,classname,name

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
# css
# tagname[attribute='value']----->input[type="submit"],  #id,  .classname,
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("kittu")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value()
#  xpath
# //tagname[@attribute='value']----->//input[@type="submit"]
driver.find_element(By.XPATH, "//input[@type='submit']").click()

txt = driver.find_element(By.CLASS_NAME, "alert-success").text
print(txt)
assert "Success!" in txt

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("heloo there")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(2)
