import time

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

enter_username = wait.until(EC.presence_of_element_located((By.NAME, "user-name")))
enter_username.send_keys("standard_user")

enter_password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
enter_password.send_keys("secret_sauce")

lick_login = wait.until(EC.presence_of_element_located((By.NAME, "login-button")))
lick_login.click()

names = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_name")))
n = len(names)

for i in range(n):
    names = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_name")))
    products = names[i].click()
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test='inventory-item-name']"))).text
    cart_Add = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[id='add-to-cart']")))
    cart_Add.click()
    print(f"✅{name} is added to cart!")
    driver.back()
    time.sleep(3)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_link"))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout"))).click()
time.sleep(3)

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']"))).send_keys("hp")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last-name']"))).send_keys("s")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']"))).send_keys("600033")


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#continue"))).click()
summ = 0
get_all_price = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_price")))
for prices in get_all_price:
    price = prices.text.replace("$","")
    summ = summ + float(price)
assert summ == 129.94

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish"))).click()
driver.save_screenshot("completed.png")












