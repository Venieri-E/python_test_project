import requests
""""List of HTTP methods"""
class http_methods:
    headers = {'Content type':'application/json'}
    cookie = ""
    @staticmethod
    def get(url):
        result = requests.get(url, headers=http_methods.headers, cookie=http_methods.cookie)
        return result

    @staticmethod
    def post(url,body):
        result = requests.post(url, headers=http_methods.headers,json=body, cookie=http_methods.cookie)
        return result

    @staticmethod
    def put(url,body):
        result = requests.put(url, headers=http_methods.headers,json=body, cookie=http_methods.cookie)
        return result

    @staticmethod
    def delete(url,body):
        result = requests.delete(url, headers=http_methods.headers,json=body, cookie=http_methods.cookie)
        return result
