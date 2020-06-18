class LoginPage:

    def __init__(self,driver):
        self.driver=driver

    def login(self,username,password):

        nombre=self.driver.find_element_by_id("nombre")
        if nombre is not None:
            nombre.send_keys(username)

        contrasena=self.driver.find_element_by_id("password")
        if contrasena is not None:
            contrasena.send_keys(password)

        login=self.driver.find_element_by_id("proceed")
        if login is not None:
            login.click()
        
        
        
