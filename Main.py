import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

btn_m1  = "/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[1]/div/button[1]" 
btn_m5  = "/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[1]/div/button[2]"
btn_m15 = "/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[1]/div/button[3]"
btn_m30 = "/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[1]/div/button[4]"
btn_h1  = "/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[1]/div/button[5]"
btn_h5  = "/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[1]/div/button[6]"
btn_d1  = "/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[1]/div/button[7]"
btn_wk  = "/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[1]/div/button[8]"
btn_mn  = "/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[1]/div/button[9]"

timeframes = [btn_m1,btn_m5,btn_m15,btn_m30,btn_h1,btn_h5,btn_d1,btn_wk,btn_mn]

#INPUTS

tf_path   = btn_m1   # Enter the Desired Timeframe here
loop_flag = True



# Set up the Chrome web driver
path = 'chromedriver.exe'

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service)
driver.get("https://www.investing.com/currencies/eur-usd-technical")

while(loop_flag):

    input_element = driver.find_element(By.XPATH,tf_path)
    input_element.click()
    time.sleep(5)
    message = driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[2]/h2")
    a = message.text
    result = a.split(":")[1]
    if result == "Buy" : 
        print("Buying with lower TP and SL")
    elif result == "Strong Buy":
        print("Buying with higher TP and SL")
    elif result == "Sell" :
        print("Selling with lower TP and SL")
    elif result == "Strong Sell" :
        print("Selling with higher TP and SL")
    else:
        print("NONE")
    time.sleep(10)
    break