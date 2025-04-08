from user_and_product_info import User,Products
from Process_Data.process import DataExtraction,Filter

from lib.logger import Logger

log=Logger("sre").get_logger()

def main():
    log.info(f"\n------- Get all user Data ---------")
    user_data=User.get_user_data()
    log.info(f"\n{user_data}")

    # log.info(f"\n\n------- Get all Products Data ---------")
    # log.info(f"\n{Products.get_products_data()}")
    
    log.info(f"\n\n-------- Lets extract important user data ---------------")

    user_lst=[]
    for item in user_data:
        # print(item)
        data=DataExtraction(item).extract_email().extract_username().extract_password().build()
        user_lst.append(data)
    log.info(f"Important user info is {user_lst}")


    log.info(f"\n\n-------------- Lets filter the data and get only what is required ---------------")
    filtered_user_data=Filter.filter_user_data(user_lst)
    log.info(f"Filtered user data is {filtered_user_data}")




if __name__=='__main__':
    main()