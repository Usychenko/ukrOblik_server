from pandas import DataFrame
from mongo import get_database

dbname = get_database()

call_name = dbname["user_1_items"]

item_detalis = call_name.find()

item_df = DataFrame(item_detalis)



print(item_df)
