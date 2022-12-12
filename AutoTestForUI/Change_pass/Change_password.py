from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import random
import string

from selenium.common.exceptions import NoSuchElementException

# Here's the connection cap for a specific phone (Xiomi redmi note 8)
desired_cap = {
    "deviceName": "UID of phone",
    "uid": "UID of phone ",
    "platformName": "Android",
    "app": "C:\\App.apk",  # Path to the apk
    "appPackage": "com.TheApp",
    "appActivity": "com.TheApp.MainActivity"}

driver = webdriver.Remote("http://localhost:port/wd/hub", desired_cap)  # local ip for connecting Appium

# Goal : Login in created account and change password.

# Script for entering email (Using XPATH because didn't have any another locators)
def enter_mail():
    loginField = driver.find_element(by=AppiumBy.XPATH,
                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
    loginField.click()
    loginField.send_keys(email)
    driver.hide_keyboard()


# We find the desired locator, call it, enter the mail, close the keyboard for further work


# Script for entering email (Using XPATH because didn't have any another locators)
def enter_pass():
    passField = driver.find_element(by=AppiumBy.XPATH,
                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
    passField.click()
    passField.send_keys(password)
    driver.hide_keyboard()


# Same for password


# Login script with passing advertising screens
def login_patient_start():
    driver.wait_activity("Log in", 5)  # Waiting for action
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log in").click()
    enter_mail()
    enter_pass()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log in").click()
    print("First login")

#  Script for entering new password
def enter_new_pass():
    passField = driver.find_element(by=AppiumBy.XPATH,
                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
    passField.click()
    passField.send_keys(new_password)

# Script for relogin after changing password
def login_patient_start_new():
    driver.implicitly_wait(5)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log in").click()
    enter_mail()
    enter_new_pass()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@content-desc=\"Log in\"]").click()
    print("Second login")


# # Interaction with menu
def tap_profile():
    profile_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile\nTab 3 of 3")
    profile_button.click()


# Script for saving profile
def save_patient_profile():
    saveProfile = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Save changes")
    saveProfile.click()


# Script for opening profile screen
def patient_profile_button():
    patient_profile_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Personal information")
    patient_profile_button.click()

# Script for changing password
def change_pass():
    change_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Change password")
    change_button.click()
    first_field = driver.find_element(by=AppiumBy.XPATH, value=
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")
    first_field.click()
    first_field.clear()
    first_field.send_keys(password)
    driver.hide_keyboard()
    second_field = driver.find_element(by=AppiumBy.XPATH, value=
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")
    second_field.click()
    second_field.clear()
    second_field.send_keys(new_password)
    driver.hide_keyboard()
    third_field = driver.find_element(by=AppiumBy.XPATH, value=
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]")
    third_field.click()
    third_field.clear()
    third_field.send_keys(new_password)
    driver.hide_keyboard()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Update password").click()


# Data for login and new password, we can enter any prepared account
email = "test11@mail.ru"
password = "1231231231"
new_password = "123123123"

# Start script
print("Start")

login_patient_start()

tap_profile()

change_pass()

# print new password for checking in manual mode
print(new_password)

# Exit from account
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Exit from account").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Exit").click()

# Entering in created account with new pass
login_patient_start_new()
