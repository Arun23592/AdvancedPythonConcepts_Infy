import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/")
driver.maximize_window()
print(driver.title)
user_name = driver.find_element(By.NAME, 'username')
pass_word = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
time.sleep(5)
user_name.send_keys("batchautomation")
pass_word.send_keys("Test@12345")
login_button.click()