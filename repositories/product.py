from models.product import Product
from utils.db import DBConnection
from utils.helpers import bson_format

from typing import List
from bson import ObjectId
from datetime import datetime


def insert(product: dict) -> None:
    with DBConnection() as conn:
        db = conn["fio-scarlet"]
        col = db["products"]
        col.insert_one(product)

def read_all() -> List:
    with DBConnection() as conn:
        db = conn["fio-scarlet"]
        col = db["products"]
        data = col.find()

        res = []
        for item in data:
            res.append(bson_format(item))
        
        return res

def update(id: str, new_product: dict) -> dict:
    with DBConnection() as conn:
        db = conn["fio-scarlet"]
        col = db["products"]

        col.replace_one({
            "_id": ObjectId(id)
            }, new_product)
        
        col.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"updated_at": datetime.now()}}
            )
        
        res = col.find_one({"_id": ObjectId(id)})
        return bson_format(res)

def delete(id: str) -> None:
    with DBConnection() as conn:
        db = conn["fio-scarlet"]
        col = db["products"]

        col.update_one(
            {"_id": ObjectId(id)}, 
            {"$set": 
                {"active": False, 
                "updated_at": datetime.now()
                }
            })