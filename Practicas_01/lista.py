import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome('Chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(2)
driver.find_element_by_link_text("REGISTER").click()
Country = Select(driver.find_element_by_name('country'))
Country.select_by_index(5)
Country.select_by_value('11')
Country.select_by_visible_text('CONGO')
time.sleep(4)
driver.quit()
