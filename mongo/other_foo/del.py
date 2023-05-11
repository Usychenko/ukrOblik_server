from mongo import get_database
import json
db = get_database()
count = 0
f = open('../some_json/add_engel.json', 'r')
dict_1 = json.load(f)
f.close()
coll = db['house']  #coll = collection
arr = [1234,2345,3456]
for i in dict_1:
    coll.delete_many({'_id':i['Meter number']})
    print(i['Meter number'])

   # count = count + 1

