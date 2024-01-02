from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\\ChromeDriver\\chromedriver-win64\\chromedriver.exe")
driver.get("https://www.ey.com/en_us")
print(driver.title)