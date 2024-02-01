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
    # main second page
    url = "https://ve.cbi.ir/TasRequest.aspx"
    national_code = "ctl00$ContentPlaceHolder1$tbIDNo" 
    phone_number = "ctl00$ContentPlaceHolder1$tbMobileNo" # use
    birth_day = "ctl00$ContentPlaceHolder1$ddlBrDay" 
    birth_year = "ctl00$ContentPlaceHolder1$tbBrYear" 
    birth_month = "ctl00$ContentPlaceHolder1$ddlBrMonth"
    marriage_day = "ctl00$ContentPlaceHolder1$ddlMarryDay"
    marriage_month = "ctl00$ContentPlaceHolder1$ddlMarryMonth" 
    marriage_year = "ctl00$ContentPlaceHolder1$tbMarrYear"
    city = "ctl00$ContentPlaceHolder1$ddlState" 
    # if's second page
    phone_number_alternetive = "ctl00$ContentPlaceHolder1$tbIDNoOwnerMobile" # use
    nationality_iran = "ctl00_ContentPlaceHolder1_rbtnMarrKind1" # use
    nationality_afghan = "ctl00_ContentPlaceHolder1_rbtnMarrKind2" # use
    nationality_no_religious = "ctl00_ContentPlaceHolder1_rbtnMarrKind3" # use
    # captchas element
    captcha_alt_page1 = "Red dot"
    captcha_id_page2 = "ctl00_ContentPlaceHolder1_ImgCaptcha"
    captcha_id_page3 = "" # add url later 
    
    # captcha fields "id"
    captcha_field_page1 = "ans"
    captcha_field_page2 = "ctl00$ContentPlaceHolder1$tbCaptcha"
    captcha_field_page3 = "" 
    
    # submit buttons
    submit_button_page1_id = "jar"
    submit_button_page1_type = "button" 
    submit_button_page2 = "ctl00$ContentPlaceHolder1$btnContinue1" # button to submit for second page
    submit_button_page3 = ""
    
    # captcha refresh buttons alt
    captcha_page1 = "bottle" 