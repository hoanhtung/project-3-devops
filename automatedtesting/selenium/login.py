# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import datetime

#driver = webdriver.Chrome()
options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Start the browser and login with standard_user
def login (user, password):
    print (timestamp(), 'Starting the browser...')

    print (timestamp(), 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    username = driver.find_element(By.ID, "user-name").send_keys(user)
    password = driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "login-button").click()
    print (timestamp(), 'User logged in: ' + user)

def addToCart():
    print (timestamp(), 'Add to cart')
    inventory_list = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for inventory_item in inventory_list:
        print(timestamp(), 'Add item to cart: ' + inventory_item.find_element(By.CLASS_NAME, "inventory_item_name").text)
        inventory_item.find_element(By.XPATH, ".//div[@class='pricebar']/button").click()

def removeFromCart():
    print (timestamp(), 'Remove from cart')
    driver.get('https://www.saucedemo.com/cart.html')
    cart_list = driver.find_elements(By.CLASS_NAME, "cart_item")
    for cart_item in cart_list:
        print(timestamp(), 'Remove item from cart: ' + cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text)
        cart_item.find_element(By.XPATH, ".//div[@class='item_pricebar']/button").click()

login('standard_user', 'secret_sauce')
addToCart()
removeFromCart()

