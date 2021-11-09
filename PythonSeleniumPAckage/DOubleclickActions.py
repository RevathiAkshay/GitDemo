import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

driver.implicitly_wait(6)

action = ActionChains(driver)
##double clicking action on a button
action.double_click(driver.find_element_by_id("double-click")).perform()

time.sleep(5)

alert = driver.switch_to.alert
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()

##to right click use context click

action.context_click(driver.find_element_by_id("double-click")).perform()