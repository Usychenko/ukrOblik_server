import pandas
import json

excel_data_df = pandas.read_excel('sample.xlsx')

json_str = excel_data_df.to_json()

f = open("new_json.json", "w")
f.write(json_str)
print('Excel Sheet to JSON:\n', json_str)
