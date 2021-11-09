## invoking Chrome Broser
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")

#Going to the exact URL
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#to induce explicit wait
time.sleep(1)

#to Provide 3 letters of the country name in the edit field
driver.find_element_by_id("autosuggest").send_keys("Ger")
time.sleep(1)

##create a list object to hold the child objects of the tag[li] which has all country names
lis1 = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

##iterate through the lis1 object and fetch the correct country and select it
for li in lis1:

    if li.text == "Germany":
        li.click()
        break

##After selection, we need to print the text appearing in the screen

print(driver.find_element_by_id("autosuggest").get_attribute("value"))
if driver.find_element_by_id("autosuggest").get_attribute("value") == "Germany":
    print("Test Passed")
else:
    print("test failed")