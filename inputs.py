#! /usr/bin/venv/python3
"""
a module that contains a class for user inputs
"""
class SignupInputs:
    """
    A class that contains attributes of user signup for a loan.
    These attributes are entered by the user with input validation.
    """
    CAPTCHA_VALUE = "60"  # Get from API solver

    def __init__(self):
        self.national_code = self.get_input("National code: ")
        self.phone_number = self.get_input("Phone number: ")
        self.birth_day = self.get_input("Birth day: ")
        self.birth_month = self.get_input("Birth month: ")
        self.birth_year = self.get_input("Birth year: ")
        self.marriage_day = self.get_input("Marriage day: ")
        self.marriage_month = self.get_input("Marriage month: ")
        self.marriage_year = self.get_input("Marriage year: ")
        self.city = self.get_string_input("City: ")
        self.submit_button = ""  # To be continued

    @staticmethod
    def get_input(prompt):
        """
        Get input from the user and perform input validation.
        """
        while True:
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    @staticmethod
    def get_string_input(prompt):
        """
        Get string input from the user.
        """
        while True:
            user_input = input(prompt)
            if user_input.isalpha():
                return user_input
            else:
                print("Invalid input. Please enter a valid string.")