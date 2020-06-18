from selenium import webdriver

browser = webdriver.Chrome('Chromedriver.exe')
browser.get('http://www.example.com')
element = browser.find_element_by_tag_name('h1')
assert element.text == 'Example Domain'
assert "More information..." in browser.page_source
browser.quit()