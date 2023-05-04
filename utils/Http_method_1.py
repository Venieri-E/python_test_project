import allure
import requests
from logger import Logger


""""List of HTTP methods"""

class Http_method:
    headers = {'Content-type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
          Logger.add_reruest(url, method="GET")
          result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
          Logger.add_response(result)
          return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_reruest(url, method="POST")
            result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_reruest(url, method="PUT")
            result = requests.put(url, headers=Http_method.headers, json=body, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_reruest(url, method="DELETE")
            result = requests.delete(url, headers=Http_method.headers, json=body, cookies=Http_method.cookie)
            Logger.add_response(result)
            return result
