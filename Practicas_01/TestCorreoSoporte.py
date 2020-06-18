import time
from selenium import webdriver
driver=webdriver.Chrome('Chromedriver.exe')
driver.get('http://automationpractice.com/index.php/')
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
email=driver.find_element_by_link_text('support@seleniumframework.com')
email.click()
time.sleep(5)
driver.quit()