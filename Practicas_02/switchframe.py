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
 
        IFrameID = driver.find_element_by_id("pruebas-iframe")
        if IFrameID is not None:
            driver.switch_to.frame(IFrameID)
            nombre=driver.find_element_by_id("Segundo")
            if nombre is not None:
                nombre.send_keys("Juan")
                
        time.sleep(3)
      
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
