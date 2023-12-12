#pip install selenium
#pip install webdriver_manager
#pip install python-dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://nl.indeed.com/")

time.sleep(1)
waarInput = driver.find_element(By.ID, "text-input-where")
submitButton = driver.find_element(By.XPATH, "//button[@type='submit']")
waarInput.send_keys("Harderwijk")
submitButton.click()
#go to harderwijk page
time.sleep(1)
popupClose = driver.find_element(By.CSS_SELECTOR, ".icl-CloseButton.icl-Card-close")
popupClose.click()
time.sleep(1)
filterRadius = driver.find_element(By.XPATH, "//button[@id='filter-radius']")
filterRadius.click()
zelfdePlaats = driver.find_element(By.LINK_TEXT, "Zelfde plaats")
zelfdePlaats.click()
time.sleep(2)
popupClose2 = driver.find_element(By.XPATH, "//button[@aria-label='sluiten']")
popupClose2.click()
time.sleep(1)
cookieClose = driver.find_element(By.ID, "onetrust-reject-all-handler")
cookieClose.click()
file = open("output.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(["COMPANIES"])
while True:
    companies = driver.find_elements(By.XPATH, "//*[@data-testid='company-name']")
    for company in companies:
        print(company.text)
        writer.writerow([company.text])
    try:
        nextPage = driver.find_element(By.XPATH, "//a[@data-testid='pagination-page-next']")
        nextPage.click()
    except NoSuchElementException:
        break
file.close()




