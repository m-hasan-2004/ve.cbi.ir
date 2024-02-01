#!/usr/bin/python3
"""
a module that contains a class for user using the app to inputs data
    * Have methods to verify given data
"""
class UserInputs:
    """
    A class that contains attributes of user signup for a loan.
    These attributes are entered by the user with input validation.
        Have 2 static methods to verify the input data based on the data type.
    """

    def __init__(self):
        self.national_code = self.get_national_code("National code: ")
        self.phone_number = self.get_phone_number("Phone number: ")
        self.birth_day = self.get_day("Birth day: ") 
        self.birth_month = self.get_month("Birth month: ")
        self.birth_year = self.get_year("Birth year: ")
        self.marriage_day = self.get_day("Marriage day: ")
        self.marriage_month = self.get_month("Marriage month: ")
        self.marriage_year = self.get_year("Marriage year: ")
        self.city = self.get_city("City: ")
        self.nationality = self.get_nationality("Nationality (1 to 3): ")
        self.phone_ownership = self.get_phone_ownership("Phone OwnerShip (1 or 2): ")

    @staticmethod
    def get_national_code(prompt: str) -> str:
        """Get national code from the user and perform input validation.
        """
        while True:
            user_input = input(prompt)
            if len(user_input) == 10 and user_input.isdigit():
                return user_input
            else:
                print("check again.")             

    @staticmethod
    def get_phone_number(prompt: str) -> str:
        """Get phone number the user and perform input validation.
        """
        while True:
            user_input = input(prompt)
            if len(user_input) == 11 and user_input.isdigit():
                return user_input
            else:
                print("check again.")             

    @staticmethod
    def get_day(prompt: str) -> str: #1 int - num >= 2 - less than 31
        """Get day of birth or marriage from the user and perform input validation.
        """
        while True:
            user_input = input(prompt)
            if (
                user_input.isdigit() and len(user_input) <= 2
                and int(user_input) <= 31 and int(user_input) != 0):
                return user_input
            else:
                print("check again.")
         
    @staticmethod
    def get_month(prompt: str) -> str:
        """Get month of birth or marriage from the user and perform input validation.
        """
        while True:
            user_input = input(prompt)
            if (
                user_input.isalpha() and len(user_input) > 1
                ):
                return user_input
            else:
                print("check again.")

    @staticmethod
    def get_year(prompt: str) -> str:
        """Get month of birth or marriage from the user and perform input validation.
        """
        while True:
            user_input = input(prompt)
            if (
                user_input.isdigit() and len(user_input) == 4
                and int(user_input) > 1300
                ):
                return user_input
            else:
                print("check again.")
    
    @staticmethod            
    def get_city(prompt: str) -> str:
        """Get city from the user and perform input validation.
        """
        while True:
            user_input = input(prompt)
            if (user_input.isalpha() and len(user_input) >= 2):
                return user_input
            else:
                print("check again.")
    @staticmethod                
    def get_nationality(prompt: str) -> int:
        """Get the nationality of user and perform validation
        1 - iranian
        2 - foreign
        3 - religious minority
        """
        while True:
            user_input = input(prompt)
            if int(user_input) <= 3 and int(user_input) != 0:
                return int(user_input)
            print("-----------------------------------------------------------------------")
            print("choose between 1 to 3\n1 - iranian\n2 - foreign\n3 - religious minority")
            print("-----------------------------------------------------------------------")
       
    @staticmethod                        
    def get_phone_ownership(prompt: str) -> int:
        """Get a number from user to choose phone number input and perform validation
        1 - for above 18
        2 - for under 18
        """
        while True:
            user_input = input(prompt)
            if int(user_input) == 1 or int(user_input) == 2:
                return int(user_input)
            print("-----------------------------------------------------------------------")
            print("choose between 1 or 2\n1 - above 18\n2 - under 18")
            print("-----------------------------------------------------------------------")