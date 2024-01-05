from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserName = "firefox"
chrome_options = Options()
chrome_options.add_argument("--headless")
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "Edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("Please print the correct browser name:" + browserName)

driver.implicitly_wait(5)
driver.get("https://login.ey.com/myey/login")
time.sleep(3)
driver.quit()