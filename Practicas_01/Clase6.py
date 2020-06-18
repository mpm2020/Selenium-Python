import time
from selenium import webdriver


driver = webdriver.Chrome('Chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(5)
try:
    assert "Welcome: Mercury Tours" in driver.title
    print("Assertion test pass")
except Exception as e:
    print("Assertion test failed", format(e))
    user_box = driver.find_element_by_name('userName')
    pass_box = driver.find_element_by_name('password')
    submit_button = driver.find_element_by_name('login')
    user_box.send_keys('test')
    pass_box.send_keys('test')
    submit_button.click()
    Register = driver.find_element_by_link_text('registration form')
    # assert Register.text == "Registration form"
    # print("Assertion test pass")
    time.sleep(5)
    driver.quit()
