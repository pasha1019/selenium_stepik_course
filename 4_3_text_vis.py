import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    button_start = browser.find_element(By.ID, 'showTextBtn')
    button_start.click()
    text_field = browser.find_element(By.ID, 'text1')
    code_pass = text_field.text
    input_field = browser.find_element(By.ID, 'userInput')
    input_field.send_keys(code_pass)
    button_check = browser.find_element(By.ID, 'checkBtn')
    button_check.click()
    time.sleep(2)
    text_field2 = browser.find_element(By.ID, 'text2')
    print(text_field2.text)
    time.sleep(5)