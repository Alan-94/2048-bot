from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser=webdriver.Firefox()
browser.get(r"https://gabrielecirulli.github.io/2048/")
browser.maximize_window()
elem = browser.find_element_by_class_name('retry-button')
htmlElem = browser.find_element_by_tag_name('html')
while True:
    try:
        htmlElem.send_keys(Keys.DOWN)
    except:
        pass
    try:
        htmlElem.send_keys(Keys.LEFT)
    except:
        pass
    try:
        htmlElem.send_keys(Keys.UP)
    except:
        pass
    try:
        htmlElem.send_keys(Keys.RIGHT)
    except:
        pass
    
    if elem.is_displayed()==True:
        time.sleep(1)
        wynik=browser.find_element_by_class_name("score-container")
        print("Koniec gry. Twój wynik to: "+wynik.text)
        break
