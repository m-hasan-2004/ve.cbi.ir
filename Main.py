#! /usr/bin/venv/python3
"""
this is the main file of the project
    using selenuim to automate the process of filling up the form of VECBI website for marriage loan
    
*** selenuim and time modules are used ***

    Signup is splited into tree segments:
        * First page of Signup that contains the possible chaptch to solve
            * Second page of Signup is for entering the personal information such as national code, phone number, birth date, etc.
                * third page is for choosing the extra info such as bank, bank branch, etc. 
"""

# importing necessary libraries
# self wrote Modules and Packages  
from HTMLTagsId import TagsId # HTML Tags
# Inputs that user should enter
from second_page_m import second_page_data_finding_entring as data_f_and_e
from second_page_m import second_page_captcha_solver as c_solve
from second_page_m import second_page_sumbit_end as submit_end
from second_page_m import UserInputs_data
from second_page_m import driver, service


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
sleep_1 = int(input("custom sleep 'sec': "))
sleep_2 = int(input("custom sleep 'sec': "))
# second page captcha
# ----------------
captchavaluep2 = ""
# ----------------

# second page submit variables
submitf1 = TagsId.submit_button_page2



# starting services 
service = service
driver = driver

data_f_and_e(url, ncode, Phone, birthd, birthm, birthy, marriaged, marriagem, marriagey, city, captchafieldp2, sleep_1, sleep_2)
# submit_end(submitf1)