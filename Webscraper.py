from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.fender.com/en-US/start")

search = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/nav/div/div/div[1]/div[3]/div/div[2]/form/input[1]')
search.send_keys("TROY SANDERS PRECISION BASS")
search.send_keys(Keys.RETURN)

time.sleep(10)