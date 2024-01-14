# importing necessary external libraries
from twocaptcha import TwoCaptcha
import os

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

api_key = os.getenv('8e9fa4bfe71cafe2df2e1f32ad64dd5e', '8e9fa4bfe71cafe2df2e1f32ad64dd5e')
image_path = '/home/hasan/Desktop/py/Automated-VECBI/captchas/captcha_image.jpg'

captcha_solution = solve_captcha(api_key, image_path)

if captcha_solution.startswith('solved:'):
    print("Captcha solution:", captcha_solution)
else:
    print("Error:", captcha_solution)
