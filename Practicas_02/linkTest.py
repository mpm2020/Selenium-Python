import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):
 def setUp(self):
     global driver
     driver=webdriver.Chrome()
     driver.get("http://www.goodstartbooks.com/pruebas")

 def testLinkText(self):
     elemento= driver.find_element_by_link_text("Pagina 2")
     if elemento is not None:
       print("Encontramos el elemento con texto Pagina 2")

 def testPartialLinkText(self):
     elemento= driver.find_element_by_partial_link_text("agina")
     if elemento is not None:
       print("Encontramos el elemento usando texto parcial")    

 def tearDown(self):
      driver.quit()

if __name__=="__main__":
   unittest.main()
