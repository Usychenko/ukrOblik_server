from mongo import get_database
import json
from csv import DictReader
import values as va
def add_new_parameters(csv_file):
    coll = get_database()[va.coll_name]
    if = open(csv_file,'r')
    arr_dict = DictReader(f)
    for d in arr_dict:
        if coll.find_one({'_id':d['Meter number']}):
            coll.update_one({'_id':d['Meter number']},{'$set':d})
        else:
            print('meter does not exist')

