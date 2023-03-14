import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://demoqa.com")
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element(By.CSS_SELECTOR, '.top-card:nth-child(1) .card-body').click()
driver.find_element(By.CSS_SELECTOR, '.element-group:nth-child(1) .menu-list > #item-1 .text').click()
#driver.find_element(By.CLASS_NAME, 'rct-icon-expand-all').click()
driver.find_element(By.CLASS_NAME, 'rct-icon-expand-close').click()
driver.find_element(By.CSS_SELECTOR, '.rct-node:nth-child(3) .rct-collapse').click()
driver.find_element(By.CSS_SELECTOR, '[for="tree-node-wordFile"] .rct-checkbox').click()
time.sleep(3)
driver.quit()