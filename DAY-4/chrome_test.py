from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())

# Launch Chrome
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

print(driver.title)

driver.quit()
