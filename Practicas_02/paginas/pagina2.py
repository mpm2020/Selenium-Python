from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Page2:
    # 1 al iniciar LoginPage(driver) se pasa driver como parametro
    def __init__(self, driver):
        self.driver = driver

    # 2 agrega una funcion login que recibe password y usuario
    # 3 copia todos las busquedas de login_prueba
    def meterNombre(self, nombre):
        # 2
        espera = WebDriverWait(self.driver, 15)
        nombre2 = espera.until(EC.element_to_be_clickable((By.ID,"Segundo")))
        if nombre2 is not None:
            nombre2.send_keys(nombre)
            print("Prueba exitosa")
            return nombre2
			

