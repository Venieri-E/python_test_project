from utils.HTTP_method import http_methods

# Methods for testing Google Maps Api"
base_url = "https://rahulshettyacademy.com" # Base URL
key = "?key=qaclick123" # Parameter for all requests


class google_maps_api():
    """Method for create new location"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
        }
        post_resourse = "/maps/api/place/add/json"  # Resourse of method POST
        post_url = base_url + post_resourse + key
        print(post_url)
