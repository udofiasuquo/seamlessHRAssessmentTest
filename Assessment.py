import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

# Answer to Task 1:

# Launch url
driver.get("https://the-internet.herokuapp.com")
# Confirm page title
print(driver.title)
# Confirm URL
print(driver.current_url)
# Click "Form Authentication"
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()
# Enter username "tomsmith"
time.sleep(1)
driver.find_element(By.NAME, "username").send_keys("tomsmith")
# Enter password "SuperSecretPassword!"
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
# Click "Login" button
time.sleep(1)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# Assert success message “You logged into a secure area!”
time.sleep(3)
successMessage = driver.find_element(By.XPATH, '//*[@id="flash"]').text
print(successMessage)
assert "You logged into a secure area!" in successMessage

print("END OF TASK 1 TEST")
print("******************************************************************************************************")

driver.minimize_window()
time.sleep(1)

# Task 2:

# Load URL
driver.get("https://the-internet.herokuapp.com")
driver.maximize_window()
# Click "Form Authentication"
time.sleep(2) 
driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
# Enter username "thomas"
time.sleep(2)
driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("thomas")
# Enter password "SecretPassword!"
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("SecretPassword!")
# Click "Login" button
time.sleep(2)
driver.find_element(By.CLASS_NAME, "radius").click()
# Assert error message “Your username is invalid!”
time.sleep(3)
errorMessage = driver.find_element(By.XPATH, '//*[@id="flash"]').text
print(errorMessage)
assert "Your username is invalid!" in errorMessage

print("END OF TASK 2 TEST")
print("******************************************************************************************************")
driver.quit()