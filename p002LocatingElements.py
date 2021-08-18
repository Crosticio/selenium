from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:

    # Locating one element
    driver.find_element(By.ID, "cheese")

    # Locating multiple elements

    mucho_cheese = driver.find_elements_by_css_selector("#cheese li")

