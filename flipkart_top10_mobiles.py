import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.flipkart.com")
driver.maximize_window()

search = driver.find_element(By.CSS_SELECTOR, ".Pke_EE")
search.send_keys("mobile")
search.send_keys(Keys.ENTER)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='DOjaWF gdgoEp col-12-12']")))

#min select filter
min_select = Select(driver.find_element(By.XPATH, "(//select[@class='Gn+jFg'])[1]"))
min_select.select_by_value("Min")

max_select = Select(driver.find_element(By.XPATH, "(//select[@class='Gn+jFg'])[2]"))
max_select.select_by_value("10000")

over_all_product = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".CGtC98")))
popularity = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='zg-M3Z'])[1]")))
popularity.click()

for i in range(10):
    over_all_product = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".CGtC98")))
    product = over_all_product[i]
    name = product.find_element(By.CSS_SELECTOR, ".KzDlHZ").text
    price = product.find_element(By.CSS_SELECTOR, "div.Nx9bqj._4b5DiR").text
    print(f"{i+1}. {name} - {price}")
time.sleep(10)
driver.quit()