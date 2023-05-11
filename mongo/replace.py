
#from dateutil import parser
from mongo import get_database

base = get_database()

coll_name = base['user_1_items']

item_0 =  {
    "_id":"U1IT00004",
    "item_name": "Bread",
    "max_discount" : "15",
    "category" : "food"
}

#coll_name.delete_one({'item_name':'Bread'})

#replace_item = coll_name.find({'item_name':'Bread'})

coll_name.replace_one({'item_name':'Bread'},item_0)

