# Project by:   ISAIAH OVIE ERNEST
# Date:         Saturday, 9th October, 2021
# Selenium bot project to Sort the prices of 4k TVS by star rating and add to cart.

import os
import time
import banggood.constants as constant
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BangGood(webdriver.Chrome):
    def __init__(self, driverPath=r"C:\SeleniumDrivers"):
        self.driverPath = driverPath
        os.environ['PATH'] += r"C:\SeleniumDrivers"
        super(BangGood, self).__init__()
    
    def goToPage(self):
        self.maximize_window()
        self.get(constant.url)

    def quitBrowser(self):
        self.quit()

    def cancelPopUp(self):
        cancel_pop_up = self.find_element_by_class_name("newuser-close")
        cancel_pop_up.click()

    def sign_up_click(self):
        sign_up_click_element = self.find_element_by_class_name("header-user")
        sign_up_click_element.click()

        time.sleep(3)
        sign_up_element = self.find_element_by_class_name("header-user-sign")
        sign_up_element.click()

    def input_email(self, myEmail):
        emailField = self.find_element_by_id("login-email")
        emailField.clear()
        emailField.send_keys(myEmail)

    def input_password(self, myPassword):
        passwordField = self.find_element_by_id("login-pwd")
        passwordField.clear()
        passwordField.send_keys(myPassword)

    def submit(self):

        time.sleep(5)
        subumitClick = self.find_element_by_id("login-submit")
        subumitClick.click()