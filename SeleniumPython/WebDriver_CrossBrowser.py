from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "Edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("Please print the correct browser name:" + browserName)

driver.implicitly_wait(5)
driver.get("https://login.ey.com/myey/login")