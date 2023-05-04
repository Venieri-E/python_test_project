from Http_method_1 import Http_method
base_url = "https://rahulshettyacademy.com" # Base URL
key = "?key=qaclick123" # Parameter for all requests
"""Method for create new location"""
class Google_maps_api():
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
        result_post = Http_method.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_place(place_id):
        """Method for get new location"""
        get_resourse = "/maps/api/place/get/json"
        get_url = base_url + get_resourse + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)
        return result_get

    def put_new_place(place_id):
        """Method for change address in location"""
        put_resourse = "/maps/api/place/update/json"  # Resourse of method PUT
        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"

        }
        result_put = Http_method.put(put_url , json_for_update_new_location)
        print(result_put.text)
        return result_put

    def delete_new_place(place_id):
        """Method for delete location"""
        delete_resourse = "/maps/api/place/delete/json"  # Resourse of method DELETE
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id,
        }
        result_delete = Http_method.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete