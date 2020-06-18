import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class ClickSelect(unittest.TestCase):
    
 def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://goodstartbooks.com/pruebas/")

 def testT1(self):
       ingredientes=driver.find_element_by_name("ingrediente");
       if ingredientes is not None:
           ingredienteSel=Select(ingredientes)
           ingredienteSel.select_by_value("cebolla")
       time.sleep(5)

 def testT2(self):
       frutas=driver.find_element_by_name("Select1");
       if frutas is not None:
           frutaSel=Select(frutas)
           frutaSel.select_by_index(1)
           frutaSel.select_by_visible_text("Sandia")
       time.sleep(5)
        
       
        
 def tearDown(self):
     driver.quit()
    

if __name__=="__main__":
   unittest.main()
