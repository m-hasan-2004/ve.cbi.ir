#!/usr/bin/python3
# importing necessary built-in libraries
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
# self wrote Modules and Packages  
from .HTMLTagsId import TagsId # HTML Tags
from .DataInputs import UserInputs # Inputs that user should enter

# Functions 
def chrome_location_func(chrome_location):
    return chrome_location

def second_page_data_finding_entring(
    url: str, ncode: str, phone: str, bday: str, bmonth: str, byear: str,
    mday: str, mmonth: str, myear: str, city: str , sleep_1: int, sleep_2: int) -> None:
    # second page of website signup 
    try:
        # Open the signup page
        driver.get(url)
        time.sleep(sleep_1)
        time.sleep(sleep_2)
        # Find the form fields and input data
        national_field = driver.find_element(By.NAME, ncode)
        phone_field = driver.find_element(By.NAME, phone)
        birth_day_field = driver.find_element(By.NAME, bday)
        birth_month_field = driver.find_element(By.NAME, bmonth)
        birth_year_field = driver.find_element(By.NAME, byear)
        marriage_day_field = driver.find_element(By.NAME, mday)
        marriage_month_field = driver.find_element(By.NAME, mmonth)
        marriage_year_field = driver.find_element(By.NAME, myear)
        city_field = driver.find_element(By.NAME, city)

        # Input the data
        national_field.send_keys(UserInputs_data.national_code)
        phone_field.send_keys(UserInputs_data.phone_number)
        birth_day_field.send_keys(UserInputs_data.birth_day)
        birth_month_field.send_keys(UserInputs_data.birth_month)
        birth_year_field.send_keys(UserInputs_data.birth_year)
        marriage_day_field.send_keys(UserInputs_data.marriage_day)
        marriage_month_field.send_keys(UserInputs_data.marriage_month)
        marriage_year_field.send_keys(UserInputs_data.marriage_year)
        city_field.send_keys(UserInputs_data.city)
      
    except Exception as e:
        print(f"something went wrong find and enter level: {e}")

def second_page_captcha_downloader():
    # Wait until the captcha image element is present
    captcha_image_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, TagsId.captcha_id_page2))
    )

    # Find the captcha image element by ID
    captcha_image_element = driver.find_element(By.ID, TagsId.captcha_id_page2)

    # Get the source URL of the captcha image
    captcha_image_url = captcha_image_element.get_attribute('src')

    # Download the captcha image
    urllib.request.urlretrieve(str(captcha_image_url), '/home/hasan/Desktop/py/Automated-VECBI/CaptchasPic/captcha_page2.jpg')

    print("Captcha image downloaded successfully.")

def second_page_submit_and_captcha(submitf1: str, captcha_result):
    try:
        # enter captcha
        driver.find_element(By.NAME, TagsId.captcha_field_page2).send_keys(captcha_result)
        
        # Submit the form
        submit_button = driver.find_element(By.NAME, submitf1)
        submit_button.click()

        # Wait for the signup process to complete (you might need to adjust the wait time)
        WebDriverWait(driver, 100).until(EC.url_changes(TagsId.url))
        time.sleep(20)

    except Exception as e:
        print(f"something went wrong | second page sumbit and end {e}")

    finally:
        # Close the browser window
        driver.quit()

# UserInputs_data class -> instance creating
UserInputs_data = UserInputs()    

# getting the chrome location
Chrome_Location = chrome_location_func('/home/hasan/Desktop/py/Automated-VECBI/NeededFiles/chromedriver')


# service and driver
service = Service(executable_path=Chrome_Location)
driver = webdriver.Chrome(service=service)


