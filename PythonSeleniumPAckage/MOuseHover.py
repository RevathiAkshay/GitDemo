from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice")

##Action chains package will be used to do mousehover on driver
action = ActionChains(driver)

#use action object then move to element method and then use the driver object to hover using perform method
action.move_to_element(driver.find_element_by_id("mousehover")).perform()

#use action object then move to element method and then use the driver object to hover/click using click and perform method
action.move_to_element(driver.find_element_by_link_text("Top")).click().perform()