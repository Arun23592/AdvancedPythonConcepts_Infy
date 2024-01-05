import webdriver_manager.chrome
from selenium.webdriver.chrome import webdriver

driver = webdriver.Chrome(webdriver_manager.ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/")