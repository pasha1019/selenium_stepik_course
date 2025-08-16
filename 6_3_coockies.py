import time
from pprint import pprint
from selenium import webdriver


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.2/index.html')
    cookies = browser.get_cookies() # all coockies
    browser.delete_all_cookies()
    time.sleep(15)
    # #cookies = browser.get_cookie('name')
    # #pprint(cookies)
    # for cookie in cookies:
    #     print(cookie['name'])  # или cookie['value'] -- перебор значений coockies
    #     elem = cookie['name']
    #     # browser.delete_cookie(f"secret_cookie_{i}") -- удаление coockie по имени
    #     # browser.delete_all_cookies() -- удаление всех coockie
    #     #if cookie['name'] == 'token_22':
    #     #    print(cookie['value'])
    # input_field = browser.find_element('xpath','//input')
    # input_field.send_keys(elem)
    # button = browser.find_element('xpath','//button')
    # button.click()
    # result = browser.find_element('xpath', "//p[@id='result']")
    # pprint(result.text)
