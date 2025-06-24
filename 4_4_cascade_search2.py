import time
from unicodedata import digit

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
    elements = browser.find_elements('xpath', "//button[@class='button']")
    for element in elements:
        element.click()
    passw = browser.find_element(By.TAG_NAME, 'password')
    print(passw.text)
    time.sleep(7)