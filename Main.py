from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import *

import time

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

# Open IEEE website
driver.get("https://www.ieee.org/")

# //*[@id="mn-signin-link"]

signin(driver)
navigate_to_cart(driver)


search_society(driver,'IEEE Education Society')
search_society(driver,'IEEE Membership')

application_XPath = "/html/body/div[4]/div[4]/div[1]/div[1]/div[6]/div[3]/div/div[2]/div[1]/div/div/div[3]/div/ul/li/a"

time.sleep(20)
application_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, application_XPath)))
application_btn.click()

org_name    = driver.find_element(by=By.ID,value='organization-name')
ad1_name    = driver.find_element(by=By.ID,value='address-line1')
ad2_name    = driver.find_element(by=By.ID,value='address-line2')
ad3_name    = driver.find_element(by=By.ID,value='address-line3')
city_name   = driver.find_element(by=By.ID,value='city')
pin_name    = driver.find_element(by=By.ID,value='postal-code')
tel_num     = driver.find_element(by=By.ID,value='postal-code')

org_name.send_keys("Symbiosis Institute of Technology")
ad1_name.send_keys("Lavale near sus gaon")
city_name.send_keys("Pune")
pin_name.send_keys("412115")
tel_num.send_keys("9384565379")

submit_XPath = "/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[5]/div[2]/div/div/div[2]/div/div[6]/div/div[2]/div/input"
submit_btn   = driver.find_element(By.XPATH, submit_XPath)

time.sleep(100)