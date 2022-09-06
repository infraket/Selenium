from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = " http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    get_one = browser.find_element(By.ID, 'num1')
    get_two = browser.find_element(By.ID, 'num2')
    x = int(get_one.text)
    y = int(get_two.text)
    a = x + y
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(a))

    button = browser.find_element('xpath', '//button[text() ="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


