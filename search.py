from selenium import webdriver
import time
import undetected_chromedriver as uc

searches = ["Selenium Python", "OpenAI ChatGPT", "Python unittest"]

for query in searches:
    driver = uc.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)
    box = driver.find_element("name", "q")
    box.send_keys(query)
    box.submit()
    print("Otsisin:", query)
    time.sleep(3)
    driver.quit()
