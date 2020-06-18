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
       opcion=driver.find_element_by_xpath("//*[@id='noImportante']/td[2]");
       if opcion is not None:
           print("texto" + opcion.text)
       time.sleep(5)

 def testT2(self):
       opcion2=driver.find_element_by_id("importante");
       if opcion2 is not None:
          valorAtributo = opcion2.get_attribute("class")
          print("Texto: " +  valorAtributo)
       time.sleep(5)
        
       
        
 def tearDown(self):
     driver.quit()
    

if __name__=="__main__":
   unittest.main()
