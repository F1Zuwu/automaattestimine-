from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

checkbox_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
checkbox_link.click()

time.sleep(1)

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

time.sleep(1)
driver.back()

input("Vajuta Enter, et brauser sulgeda...")
driver.quit()
