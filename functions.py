from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def signin(driver):
    btn_m1  = '//*[@id="mn-signin-link"]'

    input_element = driver.find_element(By.XPATH,btn_m1)
    input_element.click()

    email_field = driver.find_element(by=By.ID,value="username")
    email_field.clear()
    email_field.send_keys("n1843639@gmail.com")

    password_field = driver.find_element(by=By.ID, value="password")
    password_field.clear()
    password_field.send_keys("NVS1234#")

    submit_btn = driver.find_element(by=By.ID, value="modalWindowRegisterSignInBtn")
    submit_btn.click()

    title = driver.find_element(By.TAG_NAME, 'title')
    print(driver.title)

def navigate_to_cart(driver):
    cart_XPath = '/html/body/div[4]/header/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/span[1]/a'
# Click on cart
    cart_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cart_XPath)))

    # Click on the cart button
    cart_btn.click()

    link_XPath = '/html/body/div[4]/div[4]/div[1]/div[1]/div[3]/div/div/div[2]/div[5]/a'

    link_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link_XPath)))
    link_btn.click()

def search_society(driver, input):
    search_field = driver.find_element(by=By.ID, value="searchterms")
    search_field.clear()
    search_field.send_keys(input)

    search_btn = driver.find_element(by=By.ID, value="btn-ctlg-search")
    search_btn.click()

    result1_XPath = "/html/body/div[4]/div[4]/div[1]/div[1]/div[3]/div/div[4]/div/div[2]/div[2]/p[1]/a"
    result1_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, result1_XPath)))

    result1_button.click()
    if input == 'IEEE Membership':
        student_btn = driver.find_element(by=By.ID, value = "membership")
        time.sleep(3)
        student_btn.click()
    try:
        add_item_btn = driver.find_element(by=By.ID, value="addItems")
        time.sleep(5)
        add_item_btn.click()
        time.sleep(20)
        # add_item_btn.click()
    except Exception as e:
        print(e)