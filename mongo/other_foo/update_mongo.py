from mongo import get_database
import json
parser_engel_heat = [{'Meter number':2, 'Heat':12, 'Date':9, 'Status':11}]
parser_engel_water = [{'_id':2,'Meter number':6, 'm3':32, 'Date':31,'Status': 15}]
db = get_database()

coll = db['house'] # coll = colletion
f = open('../some_json/engel/add_engel.json','r')

#f = open(path_to_jfile, 'r')
full_dict = json.load(f)
count = 0
arr_dict = [dict for d in full_dict]
f.close()
for one_meter in full_dict:
    arr_dict[count] = one_meter
    #print(str(arr_dict[count]) + "\n")
    #print(one_meter)
    count = count + 1

for meter in arr_dict:
    if meter['Meter type'] == 'Heat':
        coll.update_one({'_id':meter['Meter number']},{'$set':
                                                       {'Parser':parser_engel_heat}})
    else:
        if meter['Meter type'] == 'Water':
            coll.update_one({'_id':meter['Meter number']},{'$set':
                                                           {'Parser':parser_engel_water}})
