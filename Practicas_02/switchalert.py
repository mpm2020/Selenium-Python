import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class ClickSelect(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://goodstartbooks.com/pruebas/")

    def test1(self):
 
        elemento = driver.find_element_by_xpath("//*[@id='center']/button")
        if elemento is not None:
            elemento.click()
        time.sleep(3)
        alerta=driver.switch_to.alert
        alerta.accept()
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
