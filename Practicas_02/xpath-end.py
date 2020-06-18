import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):
 def setUp(self):
     global driver
     driver=webdriver.Chrome()
     driver.get("http://www.goodstartbooks.com/pruebas")

 def testId(self):
     elemento= driver.find_element_by_xpath("//tr[@id='noImportante']")
     if elemento is not None:
       print("Encontramos el elemento con Id = noImportante")

 def testName(self):
     elemento= driver.find_element_by_class_name("rojo")
     if elemento is not None:
       print("Encontramos el elemento con clase name =rojo")    

 def tearDown(self):
      driver.quit()

if __name__=="__main__":
   unittest.main()
