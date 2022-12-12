from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import random
import string

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Here's the connection cap for a specific phone (Xiomi redmi note 8)
desired_cap = {
    "deviceName": "UID of phone",
    "uid": "UID of phone ",
    "platformName": "Android",
    "app": "C:\\App.apk",  # Path to the apk
    "appPackage": "com.TheApp",
    "appActivity": "com.TheApp.MainActivity"}

driver = webdriver.Remote("http://localhost:port/wd/hub", desired_cap)  # local ip for connecting Appium

# Goal : Open special screen with prepared title after login in app.


# Script for entering email (Using XPATH because didn't have any another locators)
def enter_mail():
    loginField = driver.find_element(by=AppiumBy.XPATH,
                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
    loginField.click()
    loginField.send_keys(email)
    driver.hide_keyboard()


# Script for entering password (Using XPATH because didn't have any another locators)
def enter_pass():
    passField = driver.find_element(by=AppiumBy.XPATH,
                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
    passField.click()
    passField.send_keys(password)
    driver.hide_keyboard()


# Script for login in profile
def login_patient_start():
    driver.wait_activity("Log in", 5)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log in").click()
    enter_mail()
    enter_pass()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log in").click()


# def for scrolling down
def slider_down():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(1018, 1543)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(1005, 648)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

# def for scrolling up
def slider_up():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(1025, 1539)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(1011, 655)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

# Open search
def open_find_therapist():
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search & find the best \n therapist for you")
    el1.click()

# CBT screen have special steps to reach it
def select_CBT():
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Individual difficulties").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="An adult").click()
    time.sleep(1)
    slider_down()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Less than 5 years").click()
    time.sleep(1)
    slider_down()
    time.sleep(1)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Yes").click()
    slider_down()
    time.sleep(1)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next step").click()

# Script for checking available UI
def isDisplayed(text):
    try:
        return driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=text).is_displayed()
    except:
        return False;


# Data for login, we can enter any prepared account
email = "test11@mail.ru"
password = "123123123"

# Start script
print("Start")

login_patient_start()

open_find_therapist()

select_CBT()

# Screen's title check
print(isDisplayed("Cognitive Behaviour Therapy "))
