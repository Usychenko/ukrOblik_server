from mongo import get_database
from convert import csv_to_json
import engelman_parser_insert as engel
import json
import csv
import ftp_download as f_down
import values as va

def insert_from_file(path_to_jfile):
    meters_base = get_database()
    f = open(path_to_jfile, 'r')
    full_dict = json.load(f)
    count = 0
    arr_dict = [dict for d in full_dict]
    f.close()
    for one_meter in full_dict:
        arr_dict[count] = one_meter
        count = count + 1
    meters_coll = meters_base[va.coll_name]
    for meter in arr_dict:
        if meters_coll.find_one({'_id': meter['Meter number']}):
            meters_coll.update_one({'_id': meter['Meter number']},{'$set':{
                                                                            'Heat(kWh)':meter['Heat(kWh)'],
                                                                            'Meter time':meter['Meter time'],
                                                                            'Status':meter['Status']
                                                                           }
                                                                    }
                                   )
        else:
           print('no meter')


def add_from_file(path_to_file):
    meters_base = get_database()
    f = open(path_to_file)
    count = 0
    full_dict = json.load(f)
    f.close()
    arr_dict = [dict for d in full_dict]
    meter_coll = meters_base['house']
    for one_meter in full_dict:
        arr_dict[count] = one_meter
        count = count + 1
    for meter in arr_dict:
        if meter_coll.find_one({'_id': meter['Meter number']}):
            print('Meter already exist')
        else:
            meter_coll.insert_one({'_id':meter['Meter number']})

###########################################################

#f = open('ftp_login.json','r')
#ftp_dict = json.load(f)
#f.close()

arr_json = f_down.all_csv_to_json(va.valsena_save_json,
                                  f_down.ftp_download(va.valsena_save_csv,
                                                       va.ftp_valsena,
                                                       va.ftp_url,
                                                       va.ftp_user,
                                                       va.ftp_pwd))



for jfile in arr_json:
    if jfile != '.' and jfile != '..':
        insert_from_file((jfile.replace('.csv','.json')).replace(va.csv_dir, va.json_dir))

arr_csv = f_down.ftp_download(va.engelman_save_csv,
                              va.ftp_engelman,
                              va.ftp_url,
                              va.ftp_user,
                              va.ftp_pwd)

for c_file in arr_csv:
   if c_file !='.' and c_file != '..' and ('.log' not in c_file):
        engel.update_engelman_parser(  c_file)

