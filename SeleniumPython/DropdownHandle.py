import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
driver.maximize_window()
time.sleep(4)


# def select_values(element, value):
#     select = Select(element)
#     select.select_by_visible_text(value)


def select_values_from_dropdown(dropDownOptionsList, value):
    print(len(dropDownOptionsList))
    for ele in dropDownOptionsList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break


drop_options = driver.find_elements(By.XPATH, "//select[@id='dropdowm-menu-1']")

select_values_from_dropdown(drop_options, 'Python')
select_values_from_dropdown(drop_options, 'C#')
