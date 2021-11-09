import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

l1 = []
l2 = []
driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")

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
    ##Selenium  traverse parent to child using x path
    #print(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    l1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()


print(l1)
driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait1 = WebDriverWait(driver,5)
wait1.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    l2.append(veg.text)

print(l2)

discamt1 = driver.find_element_by_class_name("discountAmt").text


driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
## CSS selector for class name can be tagname.classname
driver.find_element_by_css_selector("button.promoBtn").click()

##when implicit wait for 2 sec is used , the script failed.. if we increase the wait seconds, it will pass

wait1 = WebDriverWait(driver,8)
wait1.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

print(driver.find_element_by_css_selector(".promoInfo").text)


if l2 == l1:
    print("Delivered correct items")
else:
    print("Delivered wrong items")

assert l2 == l1

discamt2 = driver.find_element_by_class_name("discountAmt").text
if float(discamt2) < int(discamt1):
    print("Discount Applied")
else:
    print("Discount Not applied")
assert float(discamt2) <  int(discamt1)

sumt = 0

##Selenium table traverse parent to child
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
for amount in amounts:
    sumt = sumt + int(amount.text)

print(sumt)

assert sumt == int(driver.find_element_by_class_name("totAmt").text)

