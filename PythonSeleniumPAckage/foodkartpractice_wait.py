import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")

##Implicit wait- it will wait until the seconds is reached if object is not reached
##if the object is appearing within 1 sec it will resume and not wait
##if opbject does not show, it will wait for 5 sec. it is called Global wait
driver.implicitly_wait(2)

# Going to the exact URL
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

## use tagname.value for classname only
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

# selenium wait

time.sleep(4)

count = driver.find_elements_by_xpath("//div[@class='product']/h4")
assert (len(count)) == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
## CSS selector for class name can be tagname.classname
driver.find_element_by_css_selector("button.promoBtn").click()

##when implicit wait for 2 sec is used , the script failed.. if we increase the wait seconds, it will pass

print(driver.find_element_by_css_selector(".promoInfo").text)
