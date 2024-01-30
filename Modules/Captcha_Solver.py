# #!/usr/bin/python3

# importing necessary external libraries
from twocaptcha import TwoCaptcha
import time
import os

api_key = "8e9fa4bfe71cafe2df2e1f32ad64dd5e"
image_path = '/home/hasan/Desktop/py/Automated-VECBI/CaptchasPic/captcha_page2.jpg'
solver = TwoCaptcha(api_key)

def solve_captcha(
    api_key="8e9fa4bfe71cafe2df2e1f32ad64dd5e",
    image_path='/home/hasan/Desktop/py/Automated-VECBI/CaptchasPic/captcha_page2.jpg'):
    """
    Solves captcha using a JPEG file and returns a string of the result.

    Parameters:
    - api_key (str): 2Captcha API key.
    - image_path (str): Path to the captcha image file (JPEG).

    Returns:
    - str: Captcha solution or an error message.
    """
    Flag = False
    while not Flag:
        try:
            result = solver.normal(image_path)
            Flag = True
        except Exception as e:
            print(f"captcha error as {e}")
            time.sleep(2)
            Flag = False
    return result['code']

def captcha_balance():
    balance = solver.balance()
    print(f"Balance: {balance} dollars")

if __name__ == "__main__":
    solve_captcha(api_key, image_path)
    captcha_balance()