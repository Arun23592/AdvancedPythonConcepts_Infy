import time
import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.google.co.in/")
print(driver.title)
# driver.find_element(By.xpath, '//*[text()="I accept all cookies"]').click()
# driver.find_element(By.xpath, '//*[@type()="search"]').click()
driver.find_element(By.NAME, 'q').send_keys("naveen automationlab")
optionList = driver.find_elements(By.CSS_SELECTOR, 'ul.G43f7e li span')
print(len(optionList))

for ele in optionList:
    print(ele.text)
    if ele.text == 'naveen automationlabs github':
        ele.click()
        break
time.sleep(5)
driver.quit()


