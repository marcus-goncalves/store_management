import pymongo
from pymongo import MongoClient
from dotenv import dotenv_values


class DBConnection:
    def __init__(self):
        self.env = dotenv_values("./.env")
        self.uri: str = self.env["DB_URI"]
        self.connection: pymongo.database = None

    def __enter__(self):
        self.connection = MongoClient(self.uri)
        return self.connection

    def __exit__(self, _, _1, _2):
        self.connection.close()
