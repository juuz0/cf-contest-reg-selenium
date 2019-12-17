from selenium import webdriver
import time

hemail = input("Enter email/handle >  ")
passs = input("Enter password >  ")

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://codeforces.com/")

driver.find_element_by_link_text("Enter").click()

time.sleep(3)
handle = driver.find_element_by_id("handleOrEmail")
handle.send_keys(hemail)
pwd = driver.find_element_by_id("password")
pwd.send_keys(passs)
driver.find_element_by_class_name("submit").click()

time.sleep(3)

driver.find_element_by_link_text("Register now »").click()
driver.find_element_by_class_name("submit").click()

time.sleep(2)

driver.save_screenshot("success.png")

driver.close()