import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.5/index.html')
    target = browser.find_element('xpath',"//button[@id='target']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", target)
    target.click()
    time.sleep(15)