#! /usr/bin/venv/python3
"""
a module that contains a class of HTML Elements location for user data to be entered
    * this module is imported by the main .py file to use the contents of class
"""

class TagsId:
    """
    A class that contains attributes of HTML Elements location for user data to be entered.
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
    captcha_image_page1 = "" # add url later and send to class of APISolver (Hasen't Created)
    captcha_page1 = "ctl00$ContentPlaceHolder1$tbCaptcha" # captcha Field
    submit_button_page2 = "ctl00$ContentPlaceHolder1$btnContinue1" # button to submit for second page