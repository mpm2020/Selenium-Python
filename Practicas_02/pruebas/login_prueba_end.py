import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Paso 1 asegurate estos dos directorios (pruebas y paginas) estan en el path de tu computadora
from paginas.login_pagina import LoginPage
from paginas.pagina2 import Page2
import time


class ClickSendKeys(unittest.TestCase):

   def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://goodstartbooks.com/pruebas/loginTest.html")

   def testId(self):

        # Paso 2 solo creas una pagina LoginPage y llamas al metodo login.
        # todas tus pruebas
        paginaLogin = LoginPage(driver)
        paginaLogin.login("Gabriel", "Secreta")

        pagina2 = Page2(driver)
        pagina2.meterNombre("Juan")

        # no necesario, solo para que aprecies tu trabajo.      
        time.sleep(2)
      
	

   def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
