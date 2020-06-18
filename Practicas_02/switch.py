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
        #encuentra la ventana actual
        parentHandle = driver.current_window_handle
        print("Handle principal: " , parentHandle)

        #encuentra el button submit y dale clic
        driver.find_element(By.ID, "Buton1").click()
        time.sleep(3)

        #todos los handles
        todosHandles = driver.window_handles
        print("Todos los handles", todosHandles)

        for handle in todosHandles:
              if handle != parentHandle:
                  driver.switch_to.window(handle)
 
        elemento = driver.find_element_by_id("Segundo")
        if elemento is not None:
            elemento.send_keys("Juan")
        time.sleep(3)        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
