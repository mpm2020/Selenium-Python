import time
#Importamos de selenium el webdriver
from selenium import webdriver
#Creamos una instancia del driver y decimos aca te dejo el driver
driver=webdriver.Chrome('Chromedriver.exe')
# A nuestro driver creado le pasamos la url y le decimos anda a ahi
driver.get('http://www.google.com.ar')
driver.maximize_window()
time.sleep(5)
#Vamos a identificar los elementos en la pagina
texto_box=driver.find_element_by_name('q')
texto_box.send_keys('cheese')
time.sleep(2)
#busqueda_button=driver.find_element_by_name('btnK')
#busqueda_button.click()
texto_box.submit()
#Cierra el browser y termina la prueba
driver.quit()
