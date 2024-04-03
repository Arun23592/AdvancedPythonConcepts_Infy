import os.path
import time

import pytest as pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver_setup_teardown():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
    yield driver
    driver.quit()


def test_file_upload(driver_setup_teardown):
    driver = driver_setup_teardown
    filename = 'UploadFile.txt'
    file = os.path.join(os.getcwd(), filename)
    driver.get('https://the-internet.herokuapp.com/upload')
    driver.maximize_window()
    time.sleep(4)
    driver.find_element(By.ID, 'file-upload').send_keys(file)
    driver.find_element(By.ID, 'file-submit').click()
    uploaded_file = driver.find_element(By.ID, 'uploaded-files').text
    assert uploaded_file == filename, "uploaded file should be %s" % filename
