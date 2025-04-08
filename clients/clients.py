import requests
import json

from lib.logger import Logger
log=Logger("sre").get_logger()

class Client:
    @staticmethod
    def user(): 
        url = "https://fakestoreapi.com/users"
        try:
            response=requests.get(url)
            return response.json()
        except Exception as e:
            log.error(f"Exception occured during user api requests {e}")

    
    @staticmethod
    def products():
        url = "https://fakestoreapi.com/products"
        try:
            response=requests.get(url)
            return response.json()
        except Exception as e:
            log.error(f"Exception occured during product api requests {e}")