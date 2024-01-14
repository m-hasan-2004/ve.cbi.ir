#!/usr/bin/python3
"""
this is the main file of the project
    using selenuim to automate the process of filling up the form of VECBI website for marriage loan
    
*** selenuim and time modules are used ***

    Signup is splited into tree segments:
        * First page of Signup that contains the possible chaptch to solve
            * Second page of Signup is for entering the personal information such as national code, phone number, birth date, etc.
                * third page is for choosing the extra info such as bank, bank branch, etc. 
"""
# imports
import os

# self wrote Modules and Packages  
from Modules import (
    solve_captcha,
    TagsId,
)

from Modules.second_page_m import (
    second_page_data_finding_entring as data_f_and_e,
    second_page_captcha_solver as cap_solve,
    second_page_sumbit_and_end as submit_end,
    driver,
    service,
    captcha_downloader as captcha_down
)


# second page data finding variables
ncode = TagsId.national_code
url = TagsId.url
Phone = TagsId.phone_number
birthd = TagsId.birth_day
birthm = TagsId.birth_month
birthy = TagsId.birth_year
marriaged = TagsId.marriage_day
marriagem = TagsId.marriage_month
marriagey = TagsId.marriage_year
city = TagsId.city
captchafieldp2 = TagsId.captcha_field_page2
sleep_1 = 5
sleep_2 = 5
# second page captcha
# ----------------
captchavaluep2 = ""
# ----------------

# second page submit variables
submitf1 = TagsId.submit_button_page2

# captcha solving using func imported
api_key = os.getenv('8e9fa4bfe71cafe2df2e1f32ad64dd5e', '8e9fa4bfe71cafe2df2e1f32ad64dd5e')
image_path = '/home/hasan/Desktop/py/Automated-VECBI/CaptchasPic/captcha_page2.jpg'

captcha_solution = solve_captcha(api_key, image_path)

if captcha_solution.startswith('solved:'):
    print("Captcha solution:", captcha_solution)
else:
    print("Error:", captcha_solution)

# starting services 
service = service
driver = driver

data_f_and_e(
    url, ncode, Phone, birthd, birthm, birthy, marriaged,
    marriagem, marriagey, city, captchafieldp2, sleep_1,
    sleep_2)
captcha_down()
# cap_solve()
# submit_end(submitf1)