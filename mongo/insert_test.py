from mongo import get_database

from dateutil import parser

dbname = get_database()

collection_name = dbname["user_1_items"]

item_1 = {
    "_id_" : "U1IT00001",
   "item_name" : "Blender",
    "max_discount" : "10%",
    "price" : 340,
    "category" : "kitchen item"
}

item_2 = {
    "_id_" : "U1IT00002",
    "item_name" : "Egg",
    "category" : "food",
    "price" : 72
}

collection_name.insert_many([item_1, item_2])

expiry_date = '2023-04-07T00:0:000Z'
expiry = parser.parse(expiry_date)

item_3 = {
    "item_name" : "Bread",
    "quantity" : 2,
    "expiry_date" : expiry,
    "category" : "food"
}

collection_name.insert_one(item_3)

