from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.demoblaze.com/#')
btn_laptops = driver.find_element(By.LINK_TEXT, 'Laptops')
btn_laptops.click()

time.sleep(3)
btn_next = driver.find_element(By.ID, 'next2')
btn_next.click()

time.sleep(2)
info = []

items = driver.find_elements(By.CLASS_NAME, 'card')
for item in items:
    title = item.find_element(By.CLASS_NAME, 'card-title').text
    price = item.find_element(By.TAG_NAME, 'h5').text
    desc = item.find_element(By.ID, 'article').text
    info.append({'name':title, 'price':price, 'description':desc})

info_json = json.dumps(info, indent=4)
print(info_json)
driver.quit()
