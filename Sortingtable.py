from selenium import webdriver
from selenium.webdriver.common.by import By

browesersortedveg = []
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(5)
# click on coloumn header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect all veg names
vegswebele = driver.find_elements(By.XPATH, "//tr/td[1]")
for veg in vegswebele:
    browesersortedveg.append(veg.text)
originalbrowsersortedlist = browesersortedveg.copy()
# sort browser sorted vegs
browesersortedveg.sort()
# comparing both list
assert browesersortedveg == originalbrowsersortedlist
print(browesersortedveg)
print(originalbrowsersortedlist)
