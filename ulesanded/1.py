from selenium import webdriver
import time
import undetected_chromedriver as uc


driver = uc.Chrome()
driver.get("https://www.google.com")
time.sleep(2)
box = driver.find_element("name", "q")
box.send_keys("Raimo Kivi")
box.submit()
time.sleep(3)

input("Close...")