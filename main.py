#! /usr/bin/venv/python3

# importing necessary libraries and self wrote modules 
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
from fields import SignupFields as Signf
from inputs import SignupInputs as Signi

# SignupInputs / SignI -> instance creating
signup_i = Signi()    
Chrome_Location = input("enter location of chromedriver: ") or '/home/hasan/Desktop/py/Automated-VECBI/needed_files/chromedriver' 

# Start the Chrome browser (you can use other browsers by changing webdriver.Chrome to webdriver.Firefox, etc.)
service = Service(executable_path=Chrome_Location)
driver = webdriver.Chrome(service=service)

try:
    # Open the signup page
    driver.get(Signf.url)
    time.sleep(10)

    # Find the form fields and input data
    national_field = driver.find_element(By.NAME, Signf.national_code)
    phone_field = driver.find_element(By.NAME, Signf.phone_number)
    # birth_day_field = driver.find_element(By.NAME, Signf.birth_day)
    # birth_month_field = driver.find_element(By.NAME, Signf.birth_month)
    birth_year_field = driver.find_element(By.NAME, Signf.birth_year)
    # marriage_day_field = driver.find_element(By.NAME, Signf.marriage_day)
    # marriage_month_field = driver.find_element(By.NAME, Signf.marriage_month)
    marriage_year_field = driver.find_element(By.NAME, Signf.marriage_year)
    # city_field = driver.find_element(By.NAME, Signf.city)
    captcha_field = driver.find_element(By.NAME, Signf.captcha)
    
    # submit = driver.find_element(By.NAME, Signf.submit_button)
    # ...    

    # Input the data
    national_field.send_keys(signup_i.national_code)
    phone_field.send_keys(signup_i.phone_number)
    # birth_day_field.send_keys(signup_i.birth_day)
    # birth_month_field.send_keys(signup_i.birth_month)
    birth_year_field.send_keys(signup_i.birth_year)
    # marriage_day_field.send_keys(signup_i.marriage_day)
    # marriage_month_field.send_keys(signup_i.marriage_month)
    marriage_year_field.send_keys(signup_i.marriage_year)
    # city_field.send_keys(signup_i.city)
    captcha_field.send_keys(signup_i.CAPTCHA_VALUE)
    # ...
    time.sleep(10)
    # Submit the form
    submit_button = driver.find_element(By.NAME, Signf.submit_button)
    submit_button.click()

    # Wait for the signup process to complete (you might need to adjust the wait time)
    WebDriverWait(driver, 10).until(EC.url_changes(Signf.url))

    # You can add further verification steps here if needed

finally:
    # Close the browser window
    driver.quit()
