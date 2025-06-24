import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    key_element = browser.find_element(By.ID, 'secret-key-button')
    key_element.click()

    print(key_element.get_attribute("data"))
    time.sleep(3)