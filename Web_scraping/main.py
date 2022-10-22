from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


from bs4 import BeautifulSoup
from time import sleep
import time

s = Service('/Users/blakekemp/Python/Web_scraping/chromedriver')
driver = webdriver.Chrome(service=s)
# driver_two = webdriver.Chrome(PATH)
url = 'https://www.linkedin.com'
driver.get(url)
# driver_two.get('https://www.indeed.com/')
driver.set_window_size(1024, 600)
driver.maximize_window()
# Linkedin Search
link = driver.find_element(By.LINK_TEXT, 'Sign in').click()


username = "blake_kemp@yahoo.com"
password = "Bubba2018!"
job_url = "https://www.linkedin.com/jobs/search/?f_WT=2&geoId=103644278&keywords=software%20engineer%20intern&location=United%20States"
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, ".login__form button, .login__form a[role=button]").click()
time.sleep(3)
driver.get(job_url)
time.sleep(3)
driver.find_element(By.XPATH, "//button[@aria-label='Date Posted filter. Clicking this button displays all Date Posted filter options.']").click()
driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[3]/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[4]/label/p/span[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[3]/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span").click()
time.sleep(1)

try:
    if driver.find_element(By.CLASS_NAME, 'msg-overlay-list-bubble--is-minimized') is not None:
        pass
except NoSuchElementException:
    try:
        if driver.find_element(By.CLASS_NAME, 'msg-overlay-bubble-header__details flex-row align-items-center ml1') is not None:
            driver.find_element(
                By.CLASS_NAME, 'msg-overlay-bubble-header__details flex-row align-items-center ml1').click()
    except NoSuchElementException:
        pass

# Indeed Search
# string = ""
# job_desc = "Software Engineering Intern"
# job_place = ("Remote")

# driver_two.find_element_by_id("text-input-what").send_keys(job_desc)
# driver_two.find_element("text-input-where").clear()
# driver_two.find_element_by_id("text-input-where").send_keys(job_place)
# driver_two.find_element(by=By.CSS_SELECTOR, value=".yosegi-InlineWhatWhere-primaryButton").click()


job_src = driver.page_source
soup = BeautifulSoup(job_src, 'lxml')
# Job Data
jobs_block = driver.find_element(By.CSS_SELECTOR, '.jobs-search-results__list')
jobs_list = jobs_block.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
urls = driver.find_elements(By.XPATH, "//div[@CLASS='full-width artdeco-entity-lockup__title ember-view']")
link = urls.find_elements(By.TAG_NAME, 'a')
n = 0
for i in jobs_list:
    time.sleep(1)
    print("__________")
    n += 1
    #driver.execute_script("arguments[0].scrollIntoView();", jobs_list[n-1])
    print(n, i.text)

    for url in link:
        href = url.get_attribute('href')
        if href is not None:
            print(href)
        else:
            print('no link')

# Application Links
