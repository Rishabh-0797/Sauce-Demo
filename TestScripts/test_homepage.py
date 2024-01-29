import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome Driver-Chrome Browser

service_obj = Service("C://Users//Instep//PycharmProjects//SauceDemo//Driver//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)


def WebsiteLaunchTestSteps():
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(2)


def test_homepage_tc01(WebsiteLaunchTestSteps):
    global driver
    # Scenario: Get Text Swag Labs
    actual_text = driver.find_element(By.XPATH, "//div[@class='app_logo']").text
    expected_text = "Swag Labs"
    assert actual_text == expected_text


def test_homepage_tc02(WebsiteLaunchTestSteps):
    global driver
    # Scenario: Get Text Products
    actual_text = driver.find_element(By.XPATH, "//span[@class='title']").text
    expected_text = "Products"
    assert actual_text == expected_text


def test_homepage_tc03(WebsiteLaunchTestSteps):
    global driver
    # Scenario: Check Count
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(2)
    actual_text = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
    expected_text = "1"
    assert actual_text == expected_text


def test_homepage_tc04(WebsiteLaunchTestSteps):
    global driver
    # Scenario: Add/Remove Product
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()
    time.sleep(3)


# @pytest.mark.p1
def test_homepage_tc05(WebsiteLaunchTestSteps):
    global driver
    # Scenario: Check Filter
    filter_dropdown = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
    filter_dropdown.select_by_visible_text("Price (low to high)")
    time.sleep(3)


def test_homepage_tc06(WebsiteLaunchTestSteps):
    global driver
    # Scenario: Click Menu Button
    driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
    time.sleep(3)


def test_homepage_tc07(WebsiteLaunchTestSteps):
    global driver
    # Scenario: Getcopywright text
    actual_text = driver.find_element(By.XPATH, "//div[@class='footer_copy']").text
    expected_text = "© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    assert actual_text == expected_text


def test_homepage_tc08(WebsiteLaunchTestSteps):
    global driver
    # Scenario: Click Socio Button
    driver.find_element(By.XPATH, "//a[normalize-space()='LinkedIn']").click()
    time.sleep(3)
    driver.quit()
