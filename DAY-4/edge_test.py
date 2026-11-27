from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Setup EdgeDriver
service = Service(EdgeChromiumDriverManager().install())

# Launch Edge
driver = webdriver.Edge(service=service)

driver.get("https://www.google.com")

print(driver.title)

driver.quit()
