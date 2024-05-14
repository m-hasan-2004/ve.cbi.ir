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
    mday: str, mmonth: str, myear: str, city: str , wait: int) -> None:
    # second page of website signup 
    try:
        # Open the signup page
        driver.get(url)
        WebDriverWait(driver, wait).until(
        EC.presence_of_element_located((By.NAME, ncode)))
        
        # Find the form fields and input data
        national_field = driver.find_element(By.NAME, ncode).send_keys(UserInputs_data.national_code)
        if UserInputs_data.phone_ownership == 1:
            phone_ownership = driver.find_element(By.NAME, phone).send_keys(UserInputs_data.phone_number)
        elif UserInputs_data.phone_ownership == 2:
            phone_ownership = driver.find_element(By.NAME, phone).send_keys(UserInputs_data.phone_number)
         
        birth_day_field = driver.find_element(By.NAME, bday).send_keys(UserInputs_data.birth_day)
        birth_month_field = driver.find_element(By.NAME, bmonth).send_keys(UserInputs_data.birth_month)
        birth_year_field = driver.find_element(By.NAME, byear).send_keys(UserInputs_data.birth_year)
        marriage_day_field = driver.find_element(By.NAME, mday).send_keys(UserInputs_data.marriage_day)
        marriage_month_field = driver.find_element(By.NAME, mmonth).send_keys(UserInputs_data.marriage_month)
        marriage_year_field = driver.find_element(By.NAME, myear).send_keys(UserInputs_data.marriage_year)
        city_field = driver.find_element(By.NAME, city).send_keys(UserInputs_data.city)
        if UserInputs_data.nationality == 1:
            nationlity = driver.find_element(By.ID, TagsId.nationality_iran).click()
        elif UserInputs_data.nationality == 2:
            nationlity = driver.find_element(By.ID, TagsId.nationality_afghan).click()
        elif UserInputs_data.nationality == 3:
            nationlity = driver.find_element(By.ID, TagsId.nationality_no_religious).click()

    except ValueError as e:
        print(f"something went wrong find and enter level: {e}")


def second_page_captcha_downloader():
    # Wait until the captcha image element is present
    captcha_image_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, TagsId.captcha_id_page2))
    )

    # Find the captcha image element by ID
    captcha_image_element = driver.find_element(By.ID, TagsId.captcha_id_page2)

    # Get the source URL of the captcha image
    captcha_image_url = captcha_image_element.get_attribute('src')

    # Download the captcha image
    urllib.request.urlretrieve(str(captcha_image_url), '/home/hasan/Desktop/python/ve.cbi.ir/captcha_page2.jpg')

    print("Captcha image downloaded successfully.")

def second_page_submit_and_captcha(submitf1: str, captcha_result):
    try:
        # enter captcha
        driver.find_element(By.NAME, TagsId.captcha_field_page2).send_keys(captcha_result)
        
        # Submit the form
        submit_button = driver.find_element(By.NAME, submitf1)
        flag = True
        while flag:
            submit_button.click()

        # Wait for the signup process to complete (you might need to adjust the wait time)
        WebDriverWait(driver, 300).until(EC.url_changes(TagsId.url))
        time.sleep(20)

    except Exception as e:
        print(f"something went wrong | second page sumbit and end {e}")

    finally:
        # Close the browser window
        driver.quit()


# UserInputs_data class -> instance creating
UserInputs_data = UserInputs()   

# getting the chrome location
Chrome_Location = chrome_location_func(r'/home/mmdhasan/Desktop/python/ve.cbi.ir/NeededFiles/chromedriver')


# service and driver
service = Service(executable_path=Chrome_Location)
driver = webdriver.Chrome(service=service)


