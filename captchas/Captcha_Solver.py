#! usr/bin/venv/python3
""" this is a module that solves captcha using jpeg file and return a string of result
        * needs captcha_downloader.py to download captcha image
"""
#imports to use
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('8e9fa4bfe71cafe2df2e1f32ad64dd5e', '8e9fa4bfe71cafe2df2e1f32ad64dd5e')

solver = TwoCaptcha(api_key)

try:
    result = solver.normal('./captchas/captcha_image.jpg')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
    
# finally:
#     os.remove('./captchas/captcha_image.jpg')