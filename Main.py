#! /usr/bin/venv/python3
"""
this is the main file of the project
    using selenuim to automate the process of filling up the form of VECBI website for marriage loan
    
*** selenuim and time modules are used ***

    Signup is splited into tree segments:
        * First page of Signup that contains the possible chaptch to solve
            * Second page of Signup is for entering the personal information such as national code, phone number, birth date, etc.
                * third page is for choosing the extra info such as bank, bank branch, etc. 
"""

# importing necessary libraries
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
# self wrote Modules and Packages  
from HTMLTagsId import TagsId
from DataEntries import UserInputs

# getting the chrome location
Chrome_Location = input("enter location of chromedriver: ") or '/home/hasan/Desktop/py/Automated-VECBI/needed_files/chromedriver' 

# UserInputs_data -> instance creating
UserInputs_data = UserInputs()    

# Start the Chrome browser (you can use other browsers by changing webdriver.Chrome to webdriver.Firefox, etc.)
service = Service(executable_path=Chrome_Location)
driver = webdriver.Chrome(service=service)


# second page of website signup 
try:
    # Open the signup page
    driver.get(TagsId.url)
    time.sleep(0)

    # Find the form fields and input data
    national_field = driver.find_element(By.NAME, TagsId.national_code)
    phone_field = driver.find_element(By.NAME, TagsId.phone_number)
    birth_day_field = driver.find_element(By.NAME, TagsId.birth_day)
    birth_month_field = driver.find_element(By.NAME, TagsId.birth_month)
    birth_year_field = driver.find_element(By.NAME, TagsId.birth_year)
    marriage_day_field = driver.find_element(By.NAME, TagsId.marriage_day)
    marriage_month_field = driver.find_element(By.NAME, TagsId.marriage_month)
    marriage_year_field = driver.find_element(By.NAME, TagsId.marriage_year)
    city_field = driver.find_element(By.NAME, TagsId.city)
    captcha_field = driver.find_element(By.NAME, TagsId.captcha_page1) 

    # Input the data
    national_field.send_keys(UserInputs_data.national_code)
    phone_field.send_keys(UserInputs_data.phone_number)
    # birth_day_field.send_keys(UserInputs_data.birth_day)
    # birth_month_field.send_keys(UserInputs_data.birth_month)
    birth_year_field.send_keys(UserInputs_data.birth_year)
    # marriage_day_field.send_keys(UserInputs_data.marriage_day)
    # marriage_month_field.send_keys(UserInputs_data.marriage_month)
    marriage_year_field.send_keys(UserInputs_data.marriage_year)
    # city_field.send_keys(UserInputs_data.city)
    captcha_field.send_keys(UserInputs_data.captcha_value_second_page)
    # ...
    time.sleep(10)
    # Submit the form
    submit_button = driver.find_element(By.NAME, TagsId.submit_button_page2)
    submit_button.click()

    # Wait for the signup process to complete (you might need to adjust the wait time)
    WebDriverWait(driver, 10).until(EC.url_changes(TagsId.url))

    # You can add further verification steps here if needed

finally:
    # Close the browser window
    driver.quit()
