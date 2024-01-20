#!/usr/bin/python3

# importing necessary external libraries
from twocaptcha import TwoCaptcha
import time
import os

def solve_captcha(api_key="8e9fa4bfe71cafe2df2e1f32ad64dd5e", image_path='/home/hasan/Desktop/py/Automated-VECBI/CaptchasPic/captcha_page2.jpg'):
    """
    Solves captcha using a JPEG file and returns a string of the result.

    Parameters:
    - api_key (str): 2Captcha API key.
    - image_path (str): Path to the captcha image file (JPEG).

    Returns:
    - str: Captcha solution or an error message.
    """
    solver = TwoCaptcha(api_key)
    
    while True:
        try:
            result = solver.normal(image_path)
            return result["code"]

        except Exception as e:
            return str(e)
        
        # finally:
        #     os.remove("home/hasan/Desktop/py/Automated-VECBI/CaptchasPic/captcha_page2.jpg")

def main():
    start = time.time()     
    result = solve_captcha()
    print(result)
    end = time.time()
    print(end - start)
    
if __name__ == "__main__":
    main()