# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# # Chrome Driver-Chrome Browser
#
# service_obj = Service("C://Users//Instep//PycharmProjects//SauceDemo//Driver//chromedriver.exe")
#
# driver = webdriver.Chrome(service=service_obj)
#
# class
#
#
# @pytest.fixture
# def WebsiteLaunchTestSteps():
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com/")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
#     driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
#     driver.find_element(By.XPATH, "//input[@id='login-button']").click()
#     time.sleep(2)
