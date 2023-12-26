#! /usr/bin/venv/python3
"""
a module that contains a class of HTML Elements location for user data to be entered
"""

class SignupFields:
    """
    A class that contains attributes of HTML Elements location for user data to be entered.
    """
    url = "https://ve.cbi.ir/TasRequest.aspx"
    national_code = "ctl00$ContentPlaceHolder1$tbIDNo"
    phone_number = "ctl00$ContentPlaceHolder1$tbMobileNo"
    birth_day = "ctl00$ContentPlaceHolder1$ddlBrDay"
    birth_year = "ctl00$ContentPlaceHolder1$tbBrYear"
    birth_month = "ctl00$ContentPlaceHolder1$ddlBrMonth"
    marriage_day = "ctl00$ContentPlaceHolder1$ddlMarryDay"
    marriage_month = "ctl00$ContentPlaceHolder1$ddlMarryMonth"
    marriage_year = "ctl00$ContentPlaceHolder1$tbMarrYear"
    city = "ctl00$ContentPlaceHolder1$ddlState"
    captcha_image = "" # add url later and send to class of APISolver (Hasen't Created)
    captcha = "ctl00$ContentPlaceHolder1$tbCaptcha"
    submit_button = "ctl00$ContentPlaceHolder1$btnContinue1" # to be continued