import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/6/6.2/index.html")
    page_2 = browser.find_element('xpath', "//a")
    page_2.click()
    page_3 = browser.find_element('xpath', "//a")
    page_3.click()
    time.sleep(7)
    browser.back()
    time.sleep(7)
    browser.back()
    time.sleep(7)