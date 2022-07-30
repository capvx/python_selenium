import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r";C:/Selenium driver"
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(5)
element = driver.find_element(By.ID, 'downloadButton')
element.click()


progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
print(f"{progress_element.text}")
