from mongo import get_database
import json

db = get_database()

coll = db['house'] # coll = colections

f = open('../some_json/engel/add_engel.json')

dict_1 = json.load(f)

for i in dict_1:
    coll.update_one({'_id':i['Meter number']},{'$set':{'Meter type':i['Meter type']}})
   # print(i[coll.find_one({'_id':i['Meter number']})])
