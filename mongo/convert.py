import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf, delimiter = ';')

        #convert each csv row into python dict
        for row in csvReader:
            #add this python dict to json array
            jsonArray.append(row)

    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray)
        jsonf.write(jsonString)
    return jsonFilePath
#csvFilePath = 'MPC140_2023_04_25_13.csv'
#jsonFilePath = 'MPC140_2023_04_25_13.json'
#csv_to_json(csvFilePath, jsonFilePath)

