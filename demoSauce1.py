import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com")
driver.maximize_window()

#Get all usernames
get_all_usernames = wait.until(EC.presence_of_all_elements_located((By.ID, "login_credentials")))
for usernames in get_all_usernames:
    username = usernames.text.replace("Accepted usernames are:", "").strip().split("\n")
    print(username)

#Get valid password
get_password = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "login_password")))
for password_section in get_password:
    password = password_section.text.replace("Password for all users:", "").strip().split("\n")
    print(password)

#Entering username
enter_username = wait.until(EC.presence_of_element_located((By.NAME, "user-name")))
enter_username.send_keys(username[0])

#Entering password
enter_password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
enter_password.send_keys(password)

#click login button
click_login = wait.until(EC.presence_of_element_located((By.NAME, "login-button")))
click_login.click()

#load all products
load_all_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='inventory_item']")))
print(len(load_all_products))

for index, products in enumerate(load_all_products):
    name = products.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    price = products.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    print(f"{index+1}. Product Name:{name} -- Product Price: {price}")
    add_to_cart = products.find_element(By.CSS_SELECTOR, ".pricebar button")
    add_to_cart.click()
    time.sleep(3)


click_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_link"))).click()
time.sleep(2)
find_continue_shopping = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#continue-shopping"))).text
print(find_continue_shopping)

click_checkout = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout")))
click_checkout.click()

first_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']")))
first_name.send_keys("hp")

last_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last-name']")))
last_name.send_keys("s")

postal_code = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']")))
postal_code.send_keys("600033")

click_continue = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#continue")))
click_continue.click()
summ = 0
get_all_price = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_price")))
for prices in get_all_price:
    price = prices.text.replace("$","")
    summ = summ + float(price)
assert summ == 129.94