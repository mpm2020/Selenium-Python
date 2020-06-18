import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome('Chromedriver.exe')
driver.get('https://www.lavoz.com.ar/')
time.sleep(2)
#driver.find_element_by_link_text("Inmuebles").click()
Clasificacion=driver.find_element_by_xpath('/html/body/nav[1]/div/div[4]/amp-carousel/div[1]/a[7]')
Clasificacion.click()
time.sleep(20)
Inmueble=driver.find_element_by_link_text('Inmuebles')
Inmueble.click()
time.sleep(20)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
time.sleep(10)
window_after_title = driver.title
print(window_after_title)
Tipo_Inmueble = Select(driver.find_element_by_xpath('//select[@name="category"]'))
operation = Select(driver.find_element_by_name('operation'))
ubicacion = driver.find_element_by_id('town')
Tipo_Inmueble.select_by_visible_text('Casas')
operation.select_by_visible_text('Alquiler')
ubicacion.send_keys('Cordoba')
ubicacion.submit()
time.sleep(5)
print("Test OK")
driver.quit()
