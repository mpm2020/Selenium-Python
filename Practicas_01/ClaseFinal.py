import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://automationpractice.com/index.php')
driver.maximize_window()
time.sleep(5)
BotonWomen = driver.find_element_by_link_text('Women')
BotonWomen.click()
time.sleep(5)
TituloWomen = driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]')
print(TituloWomen.text)
assert TituloWomen.text == "WOMEN "
print('Se ejecuto con exito')
driver.quit()