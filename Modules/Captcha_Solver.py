#!/usr/bin/python3

# importing necessary external libraries
from twocaptcha import TwoCaptcha

def solve_captcha(api_key, image_path):
    """
    Solves captcha using a JPEG file and returns a string of the result.

    Parameters:
    - api_key (str): 2Captcha API key.
    - image_path (str): Path to the captcha image file (JPEG).

    Returns:
    - str: Captcha solution or an error message.
    """
    solver = TwoCaptcha(api_key)
    
    try:
        result = solver.normal(image_path)
        return str(result)

    except Exception as e:
        return str(e)
