import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    input_field = browser.find_element(By.ID, 'codeInput')
    input_field.send_keys('Дрогон')
    button = browser.find_element(By.ID, 'clickButton')
    button.click()
    time.sleep(5)