#!/usr/bin/python3
"""
this is the main file of the project
    using selenium to automate the process of filling up the form of VECBI website for marriage loan
    
*** selenium and time modules are used ***

    Signup is split into tree segments:
        * First page of Signup that contains the possible captcha to solve
            * Second page of Signup is for entering the personal information such as national code, phone number, etc.
                * third page is for choosing the extra info such as bank, bank branch, etc. 
"""
# imports
import time

# self wrote Modules and Packages  
from Modules import (
    solve_captcha,
    TagsId,
    api_key,
    image_path
)

from Modules.MainModules import (
    second_page_data_finding_entring as data_f_and_e,
    second_page_submit_and_captcha as submit_end,
    driver,
    service,
    second_page_captcha_downloader as captcha_down
)


# second page data finding variables
ncode = TagsId.national_code
url = TagsId.url
Phone = TagsId.phone_number
Phone_Alternative = TagsId.phone_number_alternetive
Nationality_1 = TagsId.nationality_iran
Nationality_2 = TagsId.nationality_afghan
Nationality_3 = TagsId.nationality_no_religious
birthd = TagsId.birth_day
birthm = TagsId.birth_month
birthy = TagsId.birth_year
marriaged = TagsId.marriage_day
marriagem = TagsId.marriage_month
marriagey = TagsId.marriage_year
city = TagsId.city
captchafieldp2 = TagsId.captcha_field_page2
wait = 10

# second page submit variables
submitf1 = TagsId.submit_button_page2

# starting services 
service = service
driver = driver

start_all = time.time()     
if __name__ == "__main__":
    data_f_and_e(
        url, ncode, Phone, birthd, birthm, birthy, marriaged,
        marriagem, marriagey, city, wait)
    captcha_down()
    submit_end(submitf1, solve_captcha(api_key, image_path))
    end_all = time.time()     
    print(f"final res: {end_all - start_all}")
    time.sleep(15)
