import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from paginas.login_pagina import LoginPage
from paginas.pagina2 import Page2

import time

class ClickSendKeys(unittest.TestCase):

      def setUp(self):
           global driver
           driver=webdriver.Chrome()
           driver.get("http://goodstartbooks.com/pruebas/loginTest.html")

      def testId(self):
          paginaLogin=LoginPage(driver)
          paginaLogin.login("Gabriel","Secreta")

          pagina2=Page2(driver)
          pagina2.meterNombre("Juan")

          time.sleep(2)

          
      def tearDown(self):
           driver.quit()


if __name__ == "__main__":
    unittest.main()
