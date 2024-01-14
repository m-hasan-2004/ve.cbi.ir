#!/usr/bin/python3
"""
a module that contains a class of HTML Elements location for user data to be entered
    * this module is imported by the main .py file to use the contents of class
"""

class TagsId:
    """
    A class that contains attributes of HTML Elements location for user data to be entered.
    NAME for Everything except the captchas that use ID
    """
    url = "https://ve.cbi.ir/TasRequest.aspx" # url of website to signup 
    national_code = "ctl00$ContentPlaceHolder1$tbIDNo" 
    phone_number = "ctl00$ContentPlaceHolder1$tbMobileNo" 
    birth_day = "ctl00$ContentPlaceHolder1$ddlBrDay" 
    birth_year = "ctl00$ContentPlaceHolder1$tbBrYear" 
    birth_month = "ctl00$ContentPlaceHolder1$ddlBrMonth"
    marriage_day = "ctl00$ContentPlaceHolder1$ddlMarryDay"
    marriage_month = "ctl00$ContentPlaceHolder1$ddlMarryMonth" 
    marriage_year = "ctl00$ContentPlaceHolder1$tbMarrYear"
    city = "ctl00$ContentPlaceHolder1$ddlState" #‌ city of living and bank of user
    captcha_id_page1 = "" # add url later and send to class of APISolver (Hasen't Created)
    captcha_id_page2 = "ctl00_ContentPlaceHolder1_ImgCaptcha" # add url later and send to class of APISolver (Hasen't Created)
    captcha_id_page3 = "" # add url later and send to class of APISolver (Hasen't Created)
    captcha_field_page1 = "ctl00$ContentPlaceHolder1$tbCaptcha" # captcha Field
    captcha_field_page2 = "" # captcha Field
    captcha_field_page3 = "" # captcha Field
    submit_button_page2 = "ctl00$ContentPlaceHolder1$btnContinue1" # button to submit for second page