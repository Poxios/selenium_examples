import selenium.webdriver as webdriver

search = "테스트"

driver = webdriver.Chrome()

driver.get('http://google.com')

div_elems = driver.find_element_by_class_name("gLFyf")
print(div_elems)
div_elems.send_keys(input("검색어\n"))

but_elems = driver.find_element_by_class_name("gNO89b")
print(but_elems)
but_elems.click()
