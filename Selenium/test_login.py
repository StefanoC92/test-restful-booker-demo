import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import logging

import time

#Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

@pytest.fixture(autouse=True)
def chrome_driver():

    options = Options()
    #Comment following 2 lines to Run with Chrome GUI
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-dev-shm-usage')
    #Create instance of Chrome webdriver
    driver = webdriver.Chrome(options=options)

    # implicit wait of 15 seconds
    driver.implicitly_wait(15)

    #Run web application
    driver.get("https://automationintesting.online/")

    global action 
    action = ActionChains(driver)

    yield driver

    #close the web driver
    action.reset_actions()
    driver.close()

def test_login_1(chrome_driver):
    #Set webdriver waiting time
    wt = WebDriverWait(chrome_driver, timeout=10)

    #check title of the web page
    wt.until(EC.title_is("Restful-booker-platform demo"))

    #check title of navigation bar
    wt.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='root-container']/div/nav"), "Shady Meadows B&B"))

    # check Admin link from navigation bar
    admin_link = chrome_driver.find_element(By.LINK_TEXT, "Admin")
    wt.until(EC.text_to_be_present_in_element_attribute((By.LINK_TEXT, "Admin"), "href", "https://automationintesting.online/admin"))
    # press Admin link 
    action.click(on_element= admin_link)
    action.perform()

    # check Login page is opened
    wt.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h2"), "Login"))

    # enter username
    username_txtbox = chrome_driver.find_element(By.ID, "username")
    action.click(on_element= username_txtbox).perform()
    action.send_keys("Stefano").perform()
    wt.until(EC.text_to_be_present_in_element_value((By.ID, "username"), "Stefano"))
    
    # enter password
    password_txtbox = chrome_driver.find_element(By.ID, "password")
    action.click(on_element= password_txtbox).perform()
    action.send_keys("Akjsfksjg").perform()
    wt.until(EC.text_to_be_present_in_element_value((By.ID, "password"), "Akjsfksjg"))

    # Submit credentials
    login_btn = chrome_driver.find_element(By.ID, "doLogin")
    action.click(on_element=login_btn).perform()

    # check output message
    wt.until(EC.text_to_be_present_in_element((By.TAG_NAME, "div"), "Invalid credentials"))





    

    



    
    