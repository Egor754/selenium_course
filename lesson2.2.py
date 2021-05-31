import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)
    a = num2+num1
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(a))  # ищем элемент с текстом "Python"
    button = browser.find_element_by_class_name("btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()