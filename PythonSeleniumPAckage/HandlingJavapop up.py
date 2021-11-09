from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_name("enter-name").send_keys("Revathi")
driver.find_element_by_id("alertbtn").click()

##to switch to alert mode
alert = driver.switch_to.alert
t1 = alert.text
if "Revathi" in t1:
    print("{}{}".format("Revathi"," Available in the alert pop up"))

alert.accept()

##to select OK or cancel

driver.find_element_by_id("confirmbtn").click()
alert2 = driver.switch_to.alert
print(alert2.text)
alert2.dismiss()

