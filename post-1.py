from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
url ="https://www.balticshipping.com/"
driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\wiz-1\\chromedriver.exe")
driver.maximize_window()
driver.get(url)
