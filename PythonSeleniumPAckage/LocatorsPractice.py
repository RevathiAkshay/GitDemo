from selenium import webdriver
##The webdriver will expose us to executable files. We need to give path of that excutable file which will invoke the browser
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\geckodriver.exe")
#driver = webdriver.Edge(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\msedgedriver.exe")

## get method will put the URL in the browser
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
##use locators to fill a form
#driver.find_element_by_name("name").send_keys("Revathi")
##using CSS_selector
driver.find_element_by_css_selector("input[name='name']").send_keys("Revathi")
driver.find_element_by_css_selector("input[id='exampleInputPassword1']").send_keys("Revathi")
## using name attribute
driver.find_element_by_name("email").send_keys("revathi.akshay@gmail.com")

## to select a list if the 'SELECT' class is available
#When Select clas is written , a Import of Selenium driver needs to be imported-from selenium.webdriver.support.select import Select
dropdownobj = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdownobj.select_by_visible_text("Female")
dropdownobj.select_by_index(0)
#dropdownobj.select_by_visible_text("Female")
##Select by value can be used only if Value attribute is available


##using ID attribute
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_id("inlineRadio2").click()

##using Xpath
driver.find_element_by_xpath("//input[@type='submit']").click()
bool = driver.find_element_by_class_name("alert-success").text
#print("{} {}".format("The message we got is : ",bool))

## CSS syntax
# "div[class*='alert-success']"

##xpath syntax
#"//div[contains(@class,'alert-success')]"


##adding assrtions

assert "Success" in bool
