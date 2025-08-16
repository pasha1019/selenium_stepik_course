import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new') # Запуск браузера в фоновом режиме - можно использовать без new
options_chrome.add_argument('--disable-gpu') # отключение использования графического процессора (GPU) при отрисовке
options_chrome.add_extension('coordinates.crx') # запуск с упакованным расширением. для firefox xpi
options_chrome.add_argument('user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data') # использование
                                                # профиля пользователя в тесте

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get("http://parsinger.ru/selenium/6/6.html")
    answer =  ((12434107696 * 3) * 2) + 1
    print(answer)
    input_field = browser.find_element('xpath', "//select[@id='selectId']")
    input_field.click()
    list_element = browser.find_elements('xpath', "//option")
    for el in list_element:
        if int(el.text) == answer:
            el.click()
    btn_check = browser.find_element('xpath', "//input[@id='sendbutton']")
    btn_check.click()