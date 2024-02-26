import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def select_values(options_list, value):
    for ele in drop_list:
        print(ele.text)
        if ele.text == 'value':
            ele.click()
            break


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/custom-select-drop-down-keal/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID, 'ks3KealBtn').click()
time.sleep(3)
drop_list = driver.find_elements(By.XPATH, "//*[@class='ks-menu-item']")
select_values(drop_list, 'Option 2---')

# for ele in drop_list:
#     print(ele.text)
#     if ele.text == 'Option 2---':
#         ele.click()
#         break
