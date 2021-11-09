from selenium import webdriver
##The webdriver will expose us to executable files. We need to give path of that excutable file which will invoke the browser

driver = webdriver.Chrome(executable_path="C:\\Users\Revathi Akshay\Documents\Python Selenium\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\Revathi Akshay\geckodriver.exe")

#driver = webdriver.Edge(executable_path="C:\\Users\Revathi Akshay\msedgedriver.exe")

#driver = webdriver.Ie(executable_path="C:\\Users\Revathi Akshay\IEDriverServer.exe")

## get method will put the URL in the browser
driver.get("https://rahulshettyacademy.com/")
##to get title use Title
print(driver.title)
## to print the current url
print(driver.current_url)
##To maximize the browser
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/#/learning-path")
driver.refresh()

#To go back to the previous browser
driver.back()

# to refresh
driver.refresh()

#to minimize
driver.minimize_window()

##to close the current browser
driver.close()
## to close all browsers use quit
##driver.quit()