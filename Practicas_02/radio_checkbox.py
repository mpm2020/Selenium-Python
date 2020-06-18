import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndSendKeys(unittest.TestCase):
    
 def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://goodstartbooks.com/pruebas/")

 def testT1(self):
       print("Radio buttons")
       buton1 = driver.find_element_by_id("RadioGroup1_0")
       if buton1 is not None:
            buton1.click()  
       time.sleep(5)
        
       buton2 = driver.find_element_by_id("RadioGroup1_1")
       if buton2 is not None:
            buton2.click()  
       time.sleep(5)

 def testT2(self):
        print("Checkboxes")
        buton1 = driver.find_element_by_id("CheckboxGroup1_0")
        if buton1 is not None:
            buton1.click()  
        time.sleep(5)
        
        buton2 = driver.find_element_by_id("CheckboxGroup1_1")
        if buton2 is not None:
            buton2.click()  
        time.sleep(5)
        
 def tearDown(self):
     driver.quit()
    

if __name__=="__main__":
   unittest.main()
