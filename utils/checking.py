"""Methods for check all requests"""
import json

from requests import Response

class Checking():
    """Method for check status code"""
    @staticmethod
    def check_status_code(response:Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Sucess , status code = " + str(response.status_code))
        else:
            print(("Error , status code = " + str(response.status_code)))

    @staticmethod
    def check_json_token(response: Response, expected_value):
        """The method of having a mandatory field"""
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields are aviable")

    @staticmethod
    def check_json_value(response: Response,field_name, expected_value):
        """The method of value a mandatory field"""
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " Is correct")

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
            """The method of value a mandatory field"""
            check = response.json()
            check_info = check.get(field_name)
            if search_word in check_info:
                print("Word" + " " + search_word + " " + "exist")
            else:
                print("Word" + " " + search_word + " " + "Doesnt exist")