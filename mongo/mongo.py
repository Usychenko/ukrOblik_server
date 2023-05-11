from pymongo import MongoClient
import values as va
def get_database():

    CONNECTION_STRING = "127.0.0.1"

    client = MongoClient(CONNECTION_STRING)

    return client[va.db_name]

if __name__ == "__main__":

    dbname = get_database()
    print(dbname)
