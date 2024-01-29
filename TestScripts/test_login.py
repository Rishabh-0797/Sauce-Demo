import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest

# Chrome Driver-Chrome Browser

service_obj = Service("C://Users//Instep//PycharmProjects//SauceDemo//Driver//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)


# @pytest.mark.p1
def test_login_tc1():
    global driver
    # Scenario: Login With Valid Credentials

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(2)


# @pytest.mark.p1
def test_login_tc2():
    global driver
    # Scenario: Login With Invalid Credentials
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("rishabhk")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secrget_saouce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(2)
    actual_text = driver.find_element(By.XPATH, "//h3[contains(text(),'Epic sadface: Username and password do not match a')]").text
    expected_text = "Epic sadface: Username and password do not match any user in this service"
    assert actual_text == expected_text


def test_login_tc3():
    global driver
    # Scenario: Login With blank fields
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(2)
    actual_text = driver.find_element(By.XPATH, "//h3[normalize-space()='Epic sadface: Username is required']").text
    expected_text = "Epic sadface: Username is required"
    assert actual_text == expected_text


def test_login_tc4():
    global driver
    # Scenrio: Login with either username or password empty
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("rishabh")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(2)
    actual_text = driver.find_element(By.XPATH, "//h3[normalize-space()='Epic sadface: Password is required']").text
    expected_text = "Epic sadface: Password is required"
    assert actual_text == expected_text
    driver.quit()
