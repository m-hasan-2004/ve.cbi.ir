# #!/usr/bin/python3

# importing necessary external libraries
from twocaptcha import TwoCaptcha
import time
from CaptchaApiKey import Key

api_key = Key.api_key
image_path = '/home/hasan/Desktop/python/ve.cbi.ir/captcha_page2.jpg'
solver = TwoCaptcha(api_key)


def solve_captcha(key, pic_path):
    """
    Solves captcha using a JPEG file and returns a string of the result.

    Parameters:
    - api_key (str): 2Captcha API key.
    - image_path (str): Path to the captcha image file (JPEG).

    Returns:
    - str: Captcha solution or an error message.
    """
    flag = False
    while not flag:
        try:
            result = solver.normal(image_path)
            flag = True
        except Exception as e:
            print(f"captcha error as {e}")
            time.sleep(2)
            flag = False
    return result['code']


def captcha_balance():
    """
    get the balance of captcha account - api key
    """
    balance = solver.balance()
    print(f"Balance: {balance} dollars")


if __name__ == "__main__":
    solve_captcha(api_key, image_path)
    captcha_balance()
