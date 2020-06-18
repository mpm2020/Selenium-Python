import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('Chromedriver.exe')
driver.get('http://www.google.com/')
assert "Google" in driver.title
search_box=driver.find_element_by_name('q')
search_box.send_keys('seleniumhq' + Keys.RETURN)
time.sleep(2)
try:
    driver.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except Exception as e:
    "Can't find seleniumhq"

driver.quit()