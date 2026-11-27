from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


browserName = "Chrome"
# Setup ChromeDriver
if browserName == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())

# Setup EdgeDriver
elif browserName == "FireFox":
    driver = webdriver.Firefox(GeckoDriverManager().install())

# Launch Edge
elif browserName == "Safari":
    driver = webdriver.Safari()

else:
    print("Please pass the correct browser name: "+browserName)
    raise Exception("Driver not found")

driver.implicitly_wait(5)

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID,"user-name").send_keys("performance_glitch_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()


print(driver.title)

driver.quit()
