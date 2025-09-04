from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# field'ide täitmine
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(2)

# kontrollimine kas õnnestus
success_message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in success_message:
    print("Õnnestus")
else:
    print("Ebaõnnestus")

input("Vajuta Enter, et brauser sulgeda...")
driver.quit()
