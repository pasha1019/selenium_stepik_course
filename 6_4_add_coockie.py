import time
from pprint import pprint
from selenium import webdriver


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
    cookies = browser.get_cookies() # all coockies
    browser.add_cookie({'name':'secretKey', 'value':'selenium123'})
    browser.refresh()
    time.sleep(15)
    elem = browser.find_element('xpath',"//span[@id='password']")
    print(elem.text)
