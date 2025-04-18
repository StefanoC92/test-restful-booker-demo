import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
#Comment following 2 lines to Run with Chrome GUI
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://python.org")
print(driver.title)
driver.close()

@pytest.fixture(autouse=True)
def chrome_driver():

    options = Options()
    #Comment following 2 lines to Run with Chrome GUI
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #Create instance of Chrome webdriver
    driver = webdriver.Chrome(options=options)

    # implicit wait of 15 seconds
    driver.implicitly_wait(15)

    #Run web application
    driver.get("https://automationintesting.online/")

    yield driver

    #close the web driver
    driver.close()

def test_title(chrome_driver):
    title = chrome_driver.title
    assert title == "Restful-booker-platform demo"
