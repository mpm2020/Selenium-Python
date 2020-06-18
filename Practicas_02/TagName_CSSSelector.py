import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):
    
 def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://goodstartbooks.com/pruebas/")

 def testT1(self):
        elementByTag = driver.find_element_by_tag_name("h3")
        if elementByTag is not None:
            print("Encontramos el elemento con tag = h3")

 def testT2(self):
        elementByCss = driver.find_element_by_css_selector("#primera")
        if elementByCss is not None:
            print("Encontramos el elemento con css selector #primera")

 def tearDown(self):
     driver.quit()
    

if __name__=="__main__":
   unittest.main()
