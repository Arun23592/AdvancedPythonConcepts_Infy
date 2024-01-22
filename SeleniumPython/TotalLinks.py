import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(5)
linksList = driver.find_elements(By.TAG_NAME, 'a')
print(len(linksList))

for ele in linksList:
    link_text = ele.text
    print(link_text)
    print(ele.get_attribute('href'))

imageList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imageList))

for ele in imageList:
    print(ele.get_attribute('src'))