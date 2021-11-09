import time
from select import select

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_link_text("Shop").click()

titles = driver.find_elements_by_xpath("//div[@class='card-body']/h4")
for title in titles:
    if title.text == "Blackberry":
        title.find_element_by_xpath("parent::div/parent::div/div/button").click()

driver.find_element_by_class_name("btn-primary").click()


print(driver.find_element_by_xpath("//tr/td[4]/strong").text)

driver.find_element_by_class_name("btn-success").click()

driver.find_element_by_id("country").send_keys("Ind")


wait1 = WebDriverWait(driver,10)
wait1.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

driver.find_element_by_link_text("India").click()
####CSS selector
##tage#idvalue
##tag.classname

driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
driver.find_element_by_class_name("btn-success").click()

if "Success" in driver.find_element_by_class_name("alert-success").text:
    print("order placed and test Pass")
else:
    print("order not placed and test fail")

driver.get_screenshot_as_file("Screenshot.png")





