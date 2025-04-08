from clients.clients import Client
from lib.logger import Logger

log=Logger("sre").get_logger()

class User:
    @staticmethod
    def get_user_data():
        user_data=Client.user()
        return user_data

class Products:
    @staticmethod
    def get_products_data():
        products_data=Client.products()
        return products_data
