#For selenium version 4
from selenium import webdriver
from selenium.webdriver.common.by import By

browserName = "Edge"

# Setup browser
if browserName == "Chrome":
    driver = webdriver.Chrome()

elif browserName == "Firefox":
    driver = webdriver.Firefox()

elif browserName == "Edge":
    driver = webdriver.Edge()

elif browserName == "Safari":
    driver = webdriver.Safari()

else:
    raise Exception("Driver not found: " + browserName)

driver.implicitly_wait(5)

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

print("Browser:", browserName)
print("Page Title:", driver.title)

driver.quit()
