import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.ey.com/en_us")
print(driver.title)
driver.find_element(By.xpath, '//*[text()="I accept all cookies"]').click()
driver.find_element(By.xpath, '//*[text()="Search"]').click()
driver.find_element(By.xpath, "//input[@type='search']").send_keys("AI")
time.sleep(5)


