import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def driver_setup_teardown():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
    yield driver
    driver.quit()


def test_frames(driver_setup_teardown):
    driver = driver_setup_teardown
    driver.get('https://the-internet.herokuapp.com/tinymce')
    driver.switch_to.frame('mce_0_ifr')
    editor = driver.find_element(By.ID, 'tinymce')
    before_text = editor.text
    editor.clear()
    editor.send_keys('Hello world!')
    after_text = editor.text
    assert after_text != before_text, "%s equals %s" % (before_text, after_text)
    driver.switch_to.default_content()
    assert driver.find_element(By.CSS_SELECTOR, 'h3').text != "", "h3 element should not empty"
