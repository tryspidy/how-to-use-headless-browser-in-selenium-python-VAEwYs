from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)