import urllib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd

url ="https://www.linescape.com"
driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\larvol\\chromedriver.exe")
driver.get(url)
cookie = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/a'))).click()
magnifer = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/linescape-app/div/header/div/div[1]/div')))
ul = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/linescape-app/div/header/div/div[1]/div/ul')))
serach_Bar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/linescape-app/div/header/div/div[1]/div/div/schedules-search/div")))
origin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="origin"]')))
origin.clear()
origin.send_keys('Chennai')
origin_result = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="originResults"]/div[2]/div[1]/ul')))
origin_result.click()
destination_search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="destination"]')))
destination_search.clear()
destination_search.send_keys('Cochin')
destination_result= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="destinationResults"]/div[2]/div[1]/ul')))
destination_result.click()
datepicker_val = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,'schedules-datepicker')))
datepicker_val.click()
control=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="schedules-datepicker"]/div/div[3]'))).click()
right_arrow =WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="schedules-datepicker"]/div/div[1]/div[2]')))
right_arrow.click()
claendar =WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="schedules-datepicker"]/div/div[3]')))
claendar.click()
day= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,'day-6')))
day.click()
searchButton = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.CLASS_NAME,'btn')))
ActionChains(driver).key_down(Keys.CONTROL).click(searchButton).key_up(Keys.CONTROL).perform()
driver.switch_to.window(driver.window_handles[0])
url = driver.current_url
print(url)

