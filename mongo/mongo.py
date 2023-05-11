from pymongo import MongoClient

def get_database():

    CONNECTION_STRING = "127.0.0.1"

    client = MongoClient(CONNECTION_STRING)

    return client['first']


if __name__ == "__main__":

    dbname = get_database()
    print(dbname)
