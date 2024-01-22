from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, 'input.form-control.private-form__control.login-email').send_keys('naveen30@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'input.form-control.private-form__control.login-password.m-bottom-3').send_keys('test123')
driver.find_element(By.CSS_SELECTOR, '#loginBtn').click()

