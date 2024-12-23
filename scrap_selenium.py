from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.sport.ru/")

    headlines = driver.find_elements(By.CSS_SELECTOR, ".articles-item .itm h3 a")


    with open('sport.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])  

        for headline in headlines:
            text = headline.text.strip()
            if text:  
                writer.writerow([text])

finally:
    driver.quit()