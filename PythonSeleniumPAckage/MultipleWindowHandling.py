from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")

##click to go to next window
driver.find_element_by_link_text("Click Here").click()


## to switch to child window using window_handles
driver.switch_to.window(driver.window_handles[1])

## Print the data in the child window
print(driver.find_element_by_tag_name("h3").text)

## to switch to parent window using window_handles
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)

## to switch to child window using window_handles
driver.switch_to.window(driver.window_handles[1])
driver.close()
