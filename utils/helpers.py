def bson_format(data: dict) -> dict:
    if data["_id"]:
        data["_id"] = str(data["_id"])

    return data
