from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.PARTIAL_LINK_TEXT,"Free Access to Inter").click()

win=driver.window_handles
driver.switch_to.window(win[1])
cdata=driver.find_element(By.XPATH,"//p[@class='im-para red']").text
print(cdata)
cd1=cdata.split("at")[1].strip().split(" ")[0]
print(cd1)
driver.close()
driver.switch_to.window(win[0])
driver.find_element(By.ID,"username").send_keys(cd1)
driver.find_element(By.ID,"password").send_keys(cd1)
driver.find_element(By.ID,"signInBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)