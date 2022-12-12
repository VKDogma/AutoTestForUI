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


# Goal : Create a new account and fill it


# Skip start screen and creating new account
def create_acc():
    driver.wait_activity("Log in", 5)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log in").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sign up").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Continue with Email").click()
    time.sleep(1)
    name_field = driver.find_element(by=AppiumBy.XPATH,
                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
    name_field.click()
    name_field.send_keys(name)
    driver.hide_keyboard()
    email_field = driver.find_element(by=AppiumBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
    email_field.click()
    email_field.send_keys(email)
    driver.hide_keyboard()
    pass_field = driver.find_element(by=AppiumBy.XPATH,
                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
    pass_field.click()
    pass_field.send_keys(password)
    driver.hide_keyboard()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@content-desc=\"Create an account\"]").click()
    print("Account created ")


# Interaction with menu
def tap_profile():
    profile_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile\nTab 3 of 3")
    profile_button.click()
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Fill in my profile").click()


# SCript for saving account
def save_patient_profile():
    saveProfile = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Save changes")
    saveProfile.click()


# Characters randomizer for data comparison
def random_letters(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print(rand_string)
    return rand_string


# Script for entering profile
def patient_profile_button():
    patient_profile_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Personal information")
    patient_profile_button.click()


# Script for entering name
def change_name():
    name_field = driver.find_element(by=AppiumBy.XPATH,
                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.ImageView[1]")
    name_field.click()
    driver.implicitly_wait(3)
    name_field.send_keys("name_", random_letters(3))
    driver.hide_keyboard()


# Script for entering last name
def change_lastname():
    lastname_field = driver.find_element(by=AppiumBy.XPATH,
                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.ImageView[2]")
    lastname_field.click()
    driver.implicitly_wait(3)
    lastname_field.send_keys("lastname_", random_letters(3))
    driver.hide_keyboard()


# Script for entering city
def change_city():
    city_field = driver.find_element(by=AppiumBy.XPATH,
                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.ImageView[4]")
    city_field.click()
    city_field.send_keys("city_", random_letters(3))
    driver.hide_keyboard()


# Script for entering date of birth
def change_dateOfBirth():
    dateOfBirth_field = driver.find_element(by=AppiumBy.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.ImageView[3]")
    dateOfBirth_field.click()
    dateOfBirth_field.clear()
    dateOfBirth_field.send_keys("10.10.2011")
    driver.hide_keyboard()


# Script for entering gender
def change_gender():
    non_binary = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Non-binary")
    non_binary.click()


# Script for adding new photo
def add_photo():
    change_photo = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]")
    change_photo.click()
    time.sleep(1)
    # Try needed for accept permission for access next screen
    try:
        permission = driver.find_element(by=AppiumBy.ID,
                                         value="com.android.permissioncontroller:id/permission_allow_button")
        permission.click()
    except NoSuchElementException:
        driver.find_element(by=AppiumBy.XPATH,
                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView").click()
    time.sleep(2)
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

# Script for selecting timezone
def change_timezone():

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Choose your timezone").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Astana").click()


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

def isDisplayed(text):
    try:
        return driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=text).is_displayed()
    except:
        return False;


# Data for login, we can enter any prepared account
name = "Jame"
email = "test11@mail.ru"
password = "1231231231"

# Start script
print("Start")

time.sleep(3)

# Open menu for creating account and enter in it
create_acc()

tap_profile()

#Next steps will fill profile
add_photo()

change_name()

change_lastname()

change_dateOfBirth()

change_gender()

change_city()

slider_down()

change_phone_number()

save_patient_profile()

# This method show that account was filled
print(isDisplayed("Personal information"))
