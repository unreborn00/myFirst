import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

# Get product count ONCE
product_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".hrefch")))
n = len(product_links)

for i in range(n):
    product_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".hrefch")))
    product_links[i].click()

    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".name"))).text
    price = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'$')]"))).text.replace(" *includes tax", "").strip()

    click_2_cart = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Add to cart')]")))
    click_2_cart.click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    print(f" ✅{name} is added to the card.")
    driver.back()
    driver.back()
    time.sleep(2)

