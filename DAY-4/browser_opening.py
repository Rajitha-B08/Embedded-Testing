from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://www.google.com")

print(driver.title)

driver.find_element(By.NAME,'q').send_keys("geeksForGeeks")

listes = driver.find_elements(By.CSS_SELECTOR,"ul[role='listbox'] li")
print(len(listes))

for ele in listes:
    print(ele.text)
    if ele.text == 'geeksforgeeks c programming':
        ele.click()
        break

time.sleep(10)

driver.quit()
