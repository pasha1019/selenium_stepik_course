from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Можно выбрать: "normal", "eager", "none"
page_load_strategy = "normal" # Используется по умолчанию

options = Options()
options.page_load_strategy = page_load_strategy

browser = webdriver.Chrome(options=options)