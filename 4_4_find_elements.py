import time
from unicodedata import digit

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
    elem_all = browser.find_elements(By.TAG_NAME, 'a')
    count = 0
    for elem in elem_all:
        if elem.get_attribute('stormtrooper').isnumeric():
            count += int(elem.get_attribute('stormtrooper'))
    input_field = browser.find_element('xpath', '//input')
    input_field.send_keys(count)
    button_check = browser.find_element('xpath', '//button')
    button_check.click()
    time.sleep(5)