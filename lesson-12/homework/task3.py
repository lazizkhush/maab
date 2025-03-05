from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

def scrape_laptops():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.demoblaze.com/")
    time.sleep(3)
    
    laptops = []
    
    # Click on the Laptops category
    driver.find_element(By.LINK_TEXT, "Laptops").click()
    time.sleep(3)
    
    while True:
        items = driver.find_elements(By.CLASS_NAME, "card")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "card-title").text
            price = item.find_element(By.CLASS_NAME, "card-price").text.replace("$", "")
            description = item.find_element(By.CLASS_NAME, "card-text").text
            laptops.append({"name": name, "price": price, "description": description})
        
        # Try clicking the next page button
        try:
            next_button = driver.find_element(By.LINK_TEXT, "Next")
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(3)
        except:
            break  # If no Next button, exit loop
    
    driver.quit()
    
    # Save data to JSON file
    with open("laptops.json", "w", encoding="utf-8") as f:
        json.dump(laptops, f, indent=4)
    
    print("Data saved to laptops.json")

if __name__ == "__main__":
    scrape_laptops()
