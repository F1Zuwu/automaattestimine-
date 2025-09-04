from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

# lisamine
for _ in range(5):
    add_button.click()
    time.sleep(0.2)

delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

#eemaldamine
for button in delete_buttons:
    button.click()
    time.sleep(0.2) 

input("Vajuta Enter, et brauser sulgeda...")
driver.quit()
