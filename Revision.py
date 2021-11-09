

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element_by_name("name").send_keys("Revathi")
driver.find_element_by_name("email").send_keys("revathi.akshay@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Anan1234#")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_id("inlineRadio2").click()


dropdowns = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdowns.select_by_visible_text("Female")

driver.find_element_by_class_name("btn-success").click()

assert "Success" in driver.find_element_by_class_name("alert-success").text





