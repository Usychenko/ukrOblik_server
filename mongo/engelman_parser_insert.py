from mongo import get_database
import csv
import json


def update_engelman_parser(csvFilePath):
    meters_db = get_database()
    coll = meters_db['house']
    f = open(csvFilePath,'r')
    arr_meter = csv.reader(f, delimiter = ';')
    for number in arr_meter:
        if number[0] != '«File completely written»':
         if number[2] == 'ID':
            continue
         else:
            if coll.find_one({'_id':number[2]}):
                meter = coll.find_one({'_id':number[2]})['Parser'][0]
                coll.update_one({'_id':number[2]},{'$set':{'Meter time':number[meter['Date']]}})
                if coll.find_one({'_id':number[2]})['Meter type'] == 'Heat':
                    coll.update_one({'_id':number[2]},{'$set':{'Heat':number[meter['Heat']]}})
                else:
                    if coll.find_one({'_id':number[2]})['Meter type'] == 'Water':
                        coll.update_one({'_id':number[2]},{'$set':{'m3':number[meter['m3']]}})
                coll.update_one({'_id':number[2]},{'$set':{'Meter number':number[meter['Meter number']]}})
                coll.update_one({'_id':number[2]},{'$set':{'Status':number[meter['Status']]}})
            else:
                print('no meter')
#update_engelman_parser('../some_file/engel.csv')

#engelman_convert_parser('../some_file/engel.csv', '../some_json/engel.json')
