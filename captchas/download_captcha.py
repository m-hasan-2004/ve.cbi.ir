import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import urllib.request

# getting the chrome location
Chrome_Location_Res = '/home/hasan/Desktop/py/Automated-VECBI/needed_files/chromedriver'


# service and driver
service = Service(executable_path=Chrome_Location_Res)
driver = webdriver.Chrome(service=service)

# URL of the website containing the captcha
website_url = 'https://ve.cbi.ir/TasRequest.aspx'

# ID of the captcha image element
captcha_id = "ctl00_ContentPlaceHolder1_ImgCaptcha"


# Open the website
driver.get(website_url)

# Wait until the captcha image element is present
captcha_image_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, captcha_id))
)

# Find the captcha image element by ID
captcha_image_element = driver.find_element(By.ID, captcha_id)

# Get the source URL of the captcha image
captcha_image_url = captcha_image_element.get_attribute('src')

# Download the captcha image
urllib.request.urlretrieve(captcha_image_url, '/home/hasan/Desktop/py/Automated-VECBI/captchas/captcha_image.jpg')

print("Captcha image downloaded successfully.")

driver.quit()
