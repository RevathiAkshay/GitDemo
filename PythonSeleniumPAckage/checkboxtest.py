from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")

#Going to the exact URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        if checkbox.is_selected():
            print("checkboxes checked: PASS")
        else:
            print("checkboxes not checked: FAIL")

##For selecting the Radiobuttons

##thorugh for loop
radiobuttons = driver.find_elements_by_xpath("//input[@name='radioButton']")
for radio in radiobuttons:
    if radio.get_attribute("value") == "radio3":
        radio.click()
        if radio.is_selected():
            print("Radio Button is selected")
        else:
            print("Radio Button is not selected")


##without for loop

radiobuttons = driver.find_elements_by_xpath("//input[@name='radioButton']")
radiobuttons[1].click()