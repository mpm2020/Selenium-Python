import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ClickSendKeys(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://goodstartbooks.com/pruebas/loginTest.html")

    def testId(self):

        nombre = driver.find_element_by_id("nombre")
        if nombre is not None:
            nombre.send_keys("Gabriel")

        contrasena = driver.find_element_by_name("contrasena")
        if contrasena is not None:
            contrasena.send_keys("Secreto")

        login = driver.find_element_by_id("proceed")
        if login is not None:
            login.click()

        espera = WebDriverWait(driver, 10)
        nombre2 = espera.until(EC.element_to_be_clickable((By.ID,"Segundo")))
        if nombre2 is not None:
            print("Prueba exitosa")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
