import time
from selenium import webdriver
driver=webdriver.Chrome('Chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(5)
user_box=driver.find_element_by_name('userName')
pass_box=driver.find_element_by_name('password')
submit_button=driver.find_element_by_name('login')
#Interactuar con el browser
user_box.send_keys('test')
pass_box.send_keys('test')
submit_button.click()
register=driver.find_element_by_link_text('registration form')

time.sleep(5)
driver.quit()