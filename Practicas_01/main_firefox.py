import time
#Importamos de selenium el webdriver
from selenium import webdriver
#Creamos una instancia del driver y decimos aca te dejo el driver
driver=webdriver.Firefox('geckodriver.exe')
# A nuestro driver creado le pasamos la url y le decimos anda a ahi
driver.get('http://newtours.demoaut.com/')
time.sleep(5)
#Vamos a identificar los elementos en la pagina
user_box=driver.find_element_by_name('userName')
pass_box=driver.find_element_by_name('password')
submit_button=driver.find_element_by_name('login')
#Interactuar con el browser
user_box.send_keys('test')
pass_box.send_keys('test')
submit_button.click()
time.sleep(5)
#Cierra el browser y termina la prueba
driver.quit()