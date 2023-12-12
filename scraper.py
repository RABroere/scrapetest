#pip install selenium
#pip install webdriver_manager
#pip install python-dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

load_dotenv()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://quotes.toscrape.com/")

login = driver.find_element(By.LINK_TEXT, "Login")
login.click()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
username_box = driver.find_element(By.ID, "username")
password_box = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
username_box.send_keys(username)
password_box.send_keys(password)
submit_button.click()
#logged in
while True:
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for quote in quotes:
        author = quote.find_element(By.CLASS_NAME, "author")
        keywords = quote.find_element(By.CLASS_NAME, "keywords")
        tags = keywords.get_attribute("content")
        print(author.text)
        print(tags)

    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Next").click()
    except NoSuchElementException:
        break




