from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Setup GeckoDriver
service = Service(GeckoDriverManager().install())

# Launch Firefox
driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com")

print(driver.title)

driver.quit()
