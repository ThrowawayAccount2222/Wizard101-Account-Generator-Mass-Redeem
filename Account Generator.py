from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
import string
import time

driver = webdriver.Firefox(
    executable_path=r"PATH\TO\WEBDRIVER")                       #WEBDRIVER HERE

driver.get("https://wizard101.com/user/registration")
driver.get("https://wizard101.com/user/registration")

x = 0

while True:
    start = time.time()
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    mail = username + '@gmail.com'
    Select(driver.find_element_by_id("birthDate")).select_by_value("18")
    driver.find_element_by_id('userName').send_keys(username)
    driver.find_element_by_id('password').send_keys('thisismylifenow')
    driver.find_element_by_id('passwordAgain').send_keys('thisismylifenow')
    driver.find_element_by_id('email').send_keys(mail)
    driver.find_element_by_id('emailAgain').send_keys(mail)
    driver.find_element_by_css_selector('#bp_freeplay').click()
    driver.get(('https://www.wizard101.com/auth/logout?redirectUrl=https%3A%2F%2Fwww.wizard101.com%2Fuser%2Fregistration'))

    with open("Accounts.txt", "a") as myFile:
     myFile.write(username + "\n")
    end = time.time()
    print("Username " + username + " created in " + str(end - start)[0:4] + " seconds")
    x += 1

    if x >= 250:
        x = 0
        driver.quit()
        driver = webdriver.Firefox(
            executable_path=r"PATH\TO\WEBDRIVER")                       #WEBDRIVER HERE TOO!
        driver.get("https://wizard101.com/user/registration")
        driver.get("https://wizard101.com/user/registration")
