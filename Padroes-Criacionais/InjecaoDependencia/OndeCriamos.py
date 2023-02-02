from pymongo.mongo_client import MongoClient

from api_client import ApiClient


def main():
    host = "some_host"          # these values are hardcoded
    port = 4242                 # with the assumption that
    database = "some_database"  # we can get these
    collection = "messages"     # from argparse or something

    mongo_client = MongoClient(host, port)
    database = mongo_client.get_database(database)
    message_collection = database.get_collection(collection)

    api_client = ApiClient(message_collection=message_collection)

    # api_client.get_message(...)


if __name__ == "__main__":
    main()
