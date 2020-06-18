import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('Chromedriver.exe')
driver.get('http://www.google.com/')
time.sleep(2)
search_box=driver.find_element_by_name('q')
search_box.send_keys('cheese' + Keys.RETURN)
driver.quit()

