class Page2:

    def __init__(self,driver):
        self.driver=driver

    def meterNombre(self,nombre):

       def meterNombre(self, nombre):
           
           espera = WebDriverWait(self.driver, 15)
           nombre2 = espera.until(EC.element_to_be_clickable((By.ID,"Segundo")))
           if nombre2 is not None:
               nombre2.send_keys(nombre)
               print("Prueba exitosa")
               return nombre2
        
        
