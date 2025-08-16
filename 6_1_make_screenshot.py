import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/6/6.2.1/index.html'
    browser.get(url)
    code = browser.find_element('xpath', "//div[@id='this_pic']")
    browser.save_screenshot('6_1_screen.png') # screenshot all page
    code.screenshot('6_1_el.png')
