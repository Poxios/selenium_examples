import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://google.com')

div_elems = driver.find_element_by_class_name("gLFyf")
print(div_elems)
div_elems.send_keys(input("검색어\n"))

but_elems = driver.find_element_by_class_name("gNO89b")
print(but_elems)

# but_elems.click() NOT WORK
# but_elems.send_keys(Keys.ENTER) NOT WORK

driver.execute_script("arguments[0].click();", but_elems)
