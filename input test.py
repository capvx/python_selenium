import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


os.environ['PATH'] += r";C:/Selenium driver"
driver = webdriver.Chrome()

driver.get('https://demo.anhtester.com/basic-first-form-demo.html')
driver.implicitly_wait(5)

try:
    pop_up = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    pop_up.click()
except:
    print('No element with this class name, Skipping .....')

sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
button.click()

