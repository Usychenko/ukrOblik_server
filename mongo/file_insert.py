from mongo import get_database
import json
db = get_database()

coll = db.user_1_items

f = open("new_file.json", "r")
dict_0 = json.load(f)

dict_1 = dict_0[3]['addr_info']


print(dict_1)

coll.insert_one(dict_1[0])


