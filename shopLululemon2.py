import time

from  selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://shop.lululemon.com/")
driver.maximize_window()

close_pop_up = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".closeButton__onjV4S")))
close_pop_up.click()

type_search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='nav-desktop-search']")))
type_search.send_keys("men")
type_search.send_keys(Keys.ENTER)

product_tiles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class='product-tile']")))
print(len(product_tiles))
n = len(product_tiles)

for i in range(n):
    product_tiles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class='product-tile']")))
    product_tile = product_tiles[i].click()
    name = wait.until(EC.presence_of_element_located((By.XPATH,"//h1/div"))).text
    price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[class='price-3bbvG price']"))).text
    print(f"{i + 1}. {name} - {price}")
    driver.back()
    time.sleep(3)
driver.quit()