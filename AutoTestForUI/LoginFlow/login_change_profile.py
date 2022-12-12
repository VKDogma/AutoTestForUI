import appium_flutter_finder
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium_flutter_finder import flutter_finder
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

# Goal : Open created profile and change and save all personal information

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


# Interaction with profile
def save_patient_profile():
    saveProfile = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Save changes")
    saveProfile.click()


# Characters randomizer for data comparison
def random_letters(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print(rand_string)
    return rand_string


# Interaction with profile
def Entering_profile():
    patient_profile_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Personal information")
    patient_profile_button.click()


# Script to change the name with the output of random characters
def change_name():
    # (Using XPATH because didn't have any another locators)
    name_field = driver.find_element(by=AppiumBy.XPATH,
                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.ImageView[1]")
    name_field.click()
    driver.implicitly_wait(3)
    name_field.send_keys("name_", random_letters(3))
    driver.hide_keyboard()


# Script to change the last name with the output of random characters
def change_lastname():
    # (Using XPATH because didn't have any another locators)
    lastname_field = driver.find_element(by=AppiumBy.XPATH,
                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.ImageView[2]")
    lastname_field.click()
    driver.implicitly_wait(3)
    lastname_field.send_keys("lastname_", random_letters(3))
    driver.hide_keyboard()


# Script to change the city information with the output of random characters
def change_city():
    # (Using XPATH because didn't have any another locators)
    city_field = driver.find_element(by=AppiumBy.XPATH,
                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.ImageView[4]")
    city_field.click()
    driver.implicitly_wait(3)
    city_field.send_keys("city_", random_letters(3))
    driver.hide_keyboard()


# Script to change the date of birth with prepared data
def change_date_of_birth():
    # (Using XPATH because didn't have any another locators)
    dateOfBirth_field = driver.find_element(by=AppiumBy.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.ImageView[3]")
    dateOfBirth_field.click()
    dateOfBirth_field.clear()  # By default, we had an actual date
    dateOfBirth_field.send_keys("10.10.2011")
    driver.hide_keyboard()


# Script to change the gender
def change_gender():
    non_binary = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Non-binary")
    non_binary.click()


# Script for change avatar with taking photo from gallery
def change_photo():
    photo_button = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]")
    photo_button.click()
    time.sleep(0.5)
    # Try needed for accept permission for access next screen
    try:
        permission = driver.find_element(by=AppiumBy.ID,
                                         value="com.android.permissioncontroller:id/permission_allow_button")
        permission.click()
    except NoSuchElementException:
        driver.find_element(by=AppiumBy.XPATH,
                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView").click()
    time.sleep(0.5)
    driver.find_element(by=AppiumBy.XPATH,
                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView").click()
    driver.find_element(by=AppiumBy.XPATH,
                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView").click()

    time.sleep(1)  # Loading pics
    # Doesn't have access to android part
    Taking_pic = ActionChains(driver)
    Taking_pic.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    Taking_pic.w3c_actions.pointer_action.move_to_location(209, 1245)
    Taking_pic.w3c_actions.pointer_action.pointer_down()
    Taking_pic.w3c_actions.pointer_action.pause(0.2)
    Taking_pic.w3c_actions.pointer_action.release()
    Taking_pic.perform()

    time.sleep(1)  # Loading pics

    # Select prepared pic
    bunnyPic = ActionChains(driver)
    bunnyPic.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    bunnyPic.w3c_actions.pointer_action.move_to_location(154, 1293)
    bunnyPic.w3c_actions.pointer_action.pointer_down()
    bunnyPic.w3c_actions.pointer_action.pause(0.2)
    bunnyPic.w3c_actions.pointer_action.release()
    bunnyPic.perform()


# Script for changing number
def change_phone_number():
    # TouchAction needed for scrolling screen
    TouchAction(driver).press(x=872, y=1156).move_to(x=834, y=612).release().perform()
    phone_numbers = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText")
    phone_numbers.click()
    phone_numbers.send_keys("69696969")
    # Further we used some TouchAction, because country code was a list which we can only pick
    # Open list
    TouchAction(driver).tap(x=937, y=2124).perform()
    time.sleep(1)
    # Select prepared code
    TouchAction(driver).tap(x=168, y=1801).perform()


# Data for login, we can enter any prepared account
email = "test11@mail.ru"
password = "1231231231"

# Start script
print("Start")

login_patient_start()
print("Login")

# Wait for login interation
time.sleep(7)

tap_profile()

Entering_profile()

change_photo()
print("Photo")

change_name()
print("Name")

change_lastname()
print("Last name")

change_date_of_birth()
print("Date of birth")

change_gender()
print("Gender")

change_city()
print("City")

change_phone_number()
print("Number")

# Save all changes by tapping
save_patient_profile()
