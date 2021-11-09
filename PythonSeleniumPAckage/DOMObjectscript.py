##DOM object will be owner of all the elements in ur webpage
#slenium can be used to create this DOM and exexcute
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe",options = chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element_by_name("name").send_keys("Revathi")

##to get value from edit box
print(driver.find_element_by_name("name").get_attribute("value"))

##using DOM object
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

#driver.find_element_by_link_text("Shop").click()

driver.execute_script('document.getElementsByClassName("nav-link")[1].click()')

driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

















