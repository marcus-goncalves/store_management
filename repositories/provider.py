from bson import ObjectId
from utils.db import DBConnection
from typing import List
from bson import ObjectId
from datetime import datetime


def provider_format(data: dict) -> dict:
    if data['_id']:
        data['_id'] = str(data['_id'])

    return data


def insert(provider: dict) -> None:
    with DBConnection() as conn:
        db = conn['fio-scarlet']
        col = db['providers']
        col.insert_one(provider)


def read_all() -> List:
    with DBConnection() as conn:
        db = conn['fio-scarlet']
        col = db['providers']
        data = col.find()
        res = []

        for item in data:
            res.append(provider_format(item))

        return res


def update(id: str, new_provider: dict) -> dict:
    with DBConnection() as conn:
        db = conn['fio-scarlet']
        col = db['providers']

        col.replace_one({
            "_id": ObjectId(id)
        }, new_provider)

        col.update_one({'_id': ObjectId(id)}, {
                       '$set': {'updated_at': datetime.now()}})

        res = col.find_one({"_id": ObjectId(id)})
        return provider_format(res)


def delete(id: str) -> None:
    with DBConnection() as conn:
        db = conn['fio-scarlet']
        col = db['providers']
        col.update_one({
            '_id': ObjectId(id)
        }, {
            '$set': {'active': False, 'updated_at': datetime.now()}
        })
