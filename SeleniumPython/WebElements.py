from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/30-day-free-trial")
full_name = driver.find_element(By.ID, 'Form_getForm_Name_Holder')
business_email = driver.find_element(By.ID, "Form_getForm_Email")
phone_number = driver.find_element(By.ID, "Form_getForm_Contact")
country_name = driver.find_element(By.ID, "Form_getForm_Country")

full_name.send_keys("Arun Subramani")
business_email.send_keys("aruns20@gmail.com")
phone_number.send_keys("99277806")
country_name.send_keys("India")
print(driver.title)
