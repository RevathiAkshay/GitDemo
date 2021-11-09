

 ##FOR ID alone we can create CSS in a different format
 #Syntyax - tagname#IDvalue(tagname is optional)

from selenium import webdriver
##The webdriver will expose us to executable files. We need to give path of that excutable file which will invoke the browser

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")
driver.get("https://login.salesforce.com/")
'#different format for name'
driver.find_element_by_css_selector("input#username").send_keys("RevathiNS")

 ##FOR ID alone we can create CSS in a different format
 # Syntyax - tagname.classname(tagname is optional)
driver.find_element_by_css_selector(".password").send_keys("Ananya0312")
driver.find_element_by_css_selector(".password").clear()

## use the value in the anchor for link text locator
driver.find_element_by_link_text("Forgot Your Password?").click()
##syntax for getting Xpath using text
##driver.find_element_by_xpath("//input[text()='Cancel']").click()
driver.find_element_by_xpath("//input[@value='Cancel']").click()

##Xpath and CSS selector for parent child navigation
print(driver.find_element_by_xpath("//div[@id = 'usernamegroup']/label").text)
print(driver.find_element_by_css_selector("div[id='usernamegroup'] label").text)

##xpath from grand parent tag
print(driver.find_element_by_xpath("//form[@name = 'login']/div[1]/label").text)


##CSS selector for nth child
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)

##difference between Absolute and relative Xpath
 # ## Absolute Xpath -Generating Xpath from root of HTML. This is subject to changes
 ## directly hit on the element by using the customized Xpath syntax. This is the best