import os
import time

from selenium import webdriver
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'qwe.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('qwe')
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('qwe')
    email = browser.find_element_by_name('email')
    email.send_keys('dasd')
    file = browser.find_element_by_id('file')
    file.send_keys(file_path)
    button = browser.find_element_by_class_name('btn-primary')
    button.click()
    time.sleep(1)

finally:
    time.sleep(5)
    browser.close()