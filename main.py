from selenium import webdriver
import undetected_chromedriver as uc
import time

def test_google_search():
    driver = uc.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)
    print("Avati Google")
    driver.quit()

def test_duckduckgo_search():
    driver = uc.Chrome()
    driver.get("https://duckduckgo.com")
    time.sleep(2)
    print("Avati DuckDuckGo")
    driver.quit()


test_google_search()
test_duckduckgo_search()

input("Ok.")