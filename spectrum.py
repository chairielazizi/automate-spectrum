from selenium import webdriver

import info

url = "https://casv.um.edu.my/cas/loginAllType?service=https%3A%2F%2Fspectrum.um.edu.my%2Flogin%2Findex.php"

driver = webdriver.Edge("C:/Users/user/Documents/Coding/Python/UM_spectrum/msedgedriver.exe")

driver.get(url)

driver.find_element_by_name("uname").send_keys(info.username)
driver.find_element_by_name("password").send_keys(info.password)
driver.find_element_by_name("domain").send_keys("Student")
driver.find_element_by_class_name("btn").click()

