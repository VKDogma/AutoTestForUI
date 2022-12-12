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


# Goal : Login and test payment interaction (type - free)

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


# Interaction with menu
def tap_profile():
    time.sleep(3)
    profile_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile\nTab 3 of 3")
    profile_button.click()


# Script for scrolling down
def slider_down():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(1018, 1543)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(1005, 648)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


# Script for scrolling up
def slider_up():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(1025, 1539)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(1011, 655)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


# Open menu for searching deal
def find_a_therapist():
    find_a_therapist_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                                  value="Find a Therapist to book a session")
    find_a_therapist_button.click()


# Interaction with menu
def i_know():
    i_know_toggle = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="I know")
    i_know_toggle.click()


# Script for searching deal
def therapist_name():
    namefield = driver.find_element(by=AppiumBy.XPATH,
                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View/android.view.View/android.widget.EditText")
    namefield.click()
    namefield.send_keys(Search)
    driver.hide_keyboard()


# Interaction with menu
def next_step():
    nextstep = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next step")
    nextstep.click()


# Interaction with menu
def open_profile():
    profile_becky = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="See profile")
    profile_becky.click()


# Display header validation method
def isDisplayed(text):
    try:
        return driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=text).is_displayed()
    except:
        return False;


# Data for login, we can enter any prepared account
email = "test11@mail.ru"
password = "123123123"

# Data for searching deal
Search = "Vladislav Test "

# Start script
print("Start")

login_patient_start()

find_a_therapist()

i_know()

slider_down()

# Searching deal
therapist_name()

next_step()

open_profile()

slider_down()

# Opening dealing menu
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Book session").click()

# Select terms of a transaction
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Book free consultation").click()

# Return to main manu
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Go to homepage").click()

# Checking title of deal
print(isDisplayed("My sessions"))
