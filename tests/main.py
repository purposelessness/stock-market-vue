import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from socket_config import prepare_controller, reset_controller

# Setup selenium

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('http://localhost:5173')

# Login

nav_links = driver.find_elements('xpath', '//nav/a[@href]')
profile_link = filter(lambda link: link.text == 'Profile', nav_links)
next(profile_link).click()

time.sleep(1)

login_input = driver.find_element('xpath', '//input[@id="login"]')
login_input.send_keys('admin')

submit_button = driver.find_element('xpath', '//button[@id="loginButton"]')
submit_button.click()

time.sleep(1)

profile_money_el = driver.find_element('xpath', '//span[@id="money"]')

start_money = float(profile_money_el.text)
print(f'Start money: {start_money}')

# Setup date and clock delay

prepare_controller()

# Show chart

show_stocks_button = driver.find_element('xpath', '//button[@id="showStocksButton"]')
show_stocks_button.click()

time.sleep(1)

# Buy stock

quantity_input = driver.find_element('xpath', '//input[@id="quantity"]')
quantity_input.clear()
quantity_input.send_keys('2')

buy_button = driver.find_element('xpath', '//button[@id="buyButton"]')

current_stock_price = None
while True:
    current_stock_price_el = driver.find_element('xpath', '//span[@id="stockPrice"]')
    if current_stock_price_el.text != 'None':
        current_stock_price = float(current_stock_price_el.text)
        break
    time.sleep(1)

buy_button.click()

time.sleep(2)

# Sell stock

sell_button = driver.find_element('xpath', '//button[@id="sellButton"]')

next_stock_price = None
while True:
    next_stock_price_el = driver.find_element('xpath', '//span[@id="stockPrice"]')
    if next_stock_price_el.text != 'None':
        next_stock_price = float(current_stock_price_el.text)
        break
    time.sleep(1)

sell_button.click()

# Close popup

close_popup_button = driver.find_element('xpath', '//button[@id="closePopupButton"]')
close_popup_button.click()

time.sleep(1)

# Check money

expected_money = start_money + 2 * (next_stock_price - current_stock_price)
print(f'Expected money: {expected_money}')

next_money = float(profile_money_el.text)
print(f'Next money: {next_money}')

assert math.fabs(expected_money - next_money) < 0.01

# Reset controller

reset_controller()
