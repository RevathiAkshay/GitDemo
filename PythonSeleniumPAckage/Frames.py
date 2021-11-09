from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element_by_link_text("iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("Automation test")
driver.switch_to.default_content()



