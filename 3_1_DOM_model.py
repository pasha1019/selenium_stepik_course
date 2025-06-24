from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "http://parsinger.ru/2.1/DOM/index2.html"
browser.get(url)
need_text = browser.find_element(By.ID, "text777")
print(need_text.text)
browser.quit()
