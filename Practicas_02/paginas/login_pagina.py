class LoginPage:
    # 1 al iniciar LoginPage(driver) se pasa driver como parametro
    def __init__(self, driver):
        self.driver = driver

    # 2 agrega una funcion login que recibe password y usuario
    # 3 copia todos las busquedas de login_prueba
    def login(self, username, password):
        # 2
        nombre = self.driver.find_element_by_id("nombre")
        if nombre is not None:
            nombre.send_keys(username)

        contrasena = self.driver.find_element_by_name("contrasena")
        if contrasena is not None:
            contrasena.send_keys(password)

        login = self.driver.find_element_by_id("proceed")
        if login is not None:
            login.click()
