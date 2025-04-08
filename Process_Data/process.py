from lib.logger import Logger

log=Logger("sre").get_logger()

class DataExtraction:
    def __init__(self,data):
        self.data=data
        self.user_dic={}

    def extract_email(self):
        self.user_dic['email']=self.data.get('email')
        return self

    def extract_username(self):
        self.user_dic['username']=self.data.get('username')
        return self

    def extract_password(self):
        self.user_dic['password']=self.data.get('password')
        return self

    def build(self):
        return(self.user_dic)

class Filter:
    @staticmethod
    def filter_user_data(user_lst):
        filtered_user_data=[item for item in user_lst if item['username']=='snyder']
        return filtered_user_data
