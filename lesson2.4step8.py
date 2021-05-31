import time
import math
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    but = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"),
                                                                                             "$100"))
    btn = browser.find_element_by_id('book')
    btn.click()
    # button = browser.find_element_by_id('book')
    # button.click()
    x_element = browser.find_element_by_id('input_value').text
    y = calc(x_element)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    buttons = browser.find_element_by_id("solve")
    buttons.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    browser.close()
