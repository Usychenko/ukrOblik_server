from mongo import get_database

dbname = get_database()

coll_name = dbname["user_1_items"]

item_detalis = coll_name.find()
for item in item_detalis:
        print( item)
