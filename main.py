#! /usr/bin/venv/python3

# ------------------------ imports ------------------------------ 
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    

class SignupFields:
    url = "https://ve.cbi.ir/TasRequest.aspx"
    national_code_field = "ctl00$ContentPlaceHolder1$tbIDNo"
    phone_number_field = "ctl00$ContentPlaceHolder1$tbMobileNo"
    birth_day_field = "ctl00$ContentPlaceHolder1$ddlBrDay"
    birth_year_field = "ctl00$ContentPlaceHolder1$tbBrYear"
    birth_month_field = "ctl00$ContentPlaceHolder1$ddlBrMonth"
    marriage_day_date = "ctl00$ContentPlaceHolder1$ddlMarryDay"
    marriage_month_date = "ctl00$ContentPlaceHolder1$ddlMarryMonth"
    marriage_year_date = "ctl00$ContentPlaceHolder1$tbMarrYear"
    city = "ctl00$ContentPlaceHolder1$ddlState"
    capthcha_image = "" # add url later and send to class of APISolver (Hasen't Created)
    capthcha_field = "ctl00$ContentPlaceHolder1$tbCaptcha"
    submit_button = "" # to be continued
    

class SignUpInputs:
    National_code = input("National code: ")
    phone_number = input("Phone number: ")
    # birth_day = input("Birth day: ")
    # birth_month = input("Birth month: ")
    birth_year = input("Birth year: ")
    # marriage_day = input("Marriage day: ")
    # marriage_month = input("Marriage month: ")
    marriage_year = input("Marriage year: ")
    # city = input("City: ")
    capthcha = "60" # get from api solver
    # submit_button = "" # to be continued


# Start the Chrome browser (you can use other browsers by changing webdriver.Chrome to webdriver.Firefox, etc.)
service = Service(executable_path='/home/hasan/Desktop/CodesFile/Automated-VECBI/needed_files/chromedriver')
driver = webdriver.Chrome(service=service)

try:
    # Open the signup page
    driver.get(SignupFields.url)
    time.sleep(10)

    # Find the form fields and input data
    national_field = driver.find_element(By.NAME, SignupFields.national_code_field)
    phone_field = driver.find_element(By.NAME, SignupFields.phone_number_field)
    # birth_day_field = driver.find_element(By.NAME, SignupFields.birth_day_field)
    # birth_month_field = driver.find_element(By.NAME, SignupFields.birth_month_field)
    birth_year_field = driver.find_element(By.NAME, SignupFields.birth_year_field)
    # marriage_day_field = driver.find_element(By.NAME, SignupFields.marriage_day_date)
    # marriage_month_field = driver.find_element(By.NAME, SignupFields.marriage_month_date)
    marriage_year_field = driver.find_element(By.NAME, SignupFields.marriage_year_date)
    # city_field = driver.find_element(By.NAME, SignupFields.city)
    captcha_field = driver.find_element(By.NAME, SignupFields.capthcha_field)
    
    # submit = driver.find_element(By.NAME, SignupFields.submit_button)
    # ...    

    # Input the data
    national_field.send_keys(SignUpInputs.National_code)
    phone_field.send_keys(SignUpInputs.phone_number)
    # birth_day_field.send_keys(SignUpInputs.birth_day)
    # birth_month_field.send_keys(SignUpInputs.birth_month)
    birth_year_field.send_keys(SignUpInputs.birth_year)
    # marriage_day_field.send_keys(SignUpInputs.marriage_day)
    # marriage_month_field.send_keys(SignUpInputs.marriage_month)
    marriage_year_field.send_keys(SignUpInputs.marriage_year)
    # city_field.send_keys(SignUpInputs.city)
    captcha_field.send_keys(SignUpInputs.capthcha)
    # ...
    time.sleep(10)
    # Submit the form
    submit_button = driver.find_element(By.NAME, SignupFields.submit_button_name)
    submit_button.click()

    # Wait for the signup process to complete (you might need to adjust the wait time)
    WebDriverWait(driver, 10).until(EC.url_changes(SignupFields.url))

    # You can add further verification steps here if needed

finally:
    # Close the browser window
    driver.quit()
