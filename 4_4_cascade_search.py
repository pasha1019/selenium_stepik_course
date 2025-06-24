import time
from unicodedata import digit

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    parent_el = browser.find_element('xpath', "//div[@id='parent_id']")
    child_el = parent_el.find_element('xpath', "//div[@class='child_class']")
    child_el.click()
    print(child_el.get_attribute('password'))


