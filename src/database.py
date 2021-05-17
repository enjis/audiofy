from typing import List, Dict
from pymongo import MongoClient
from constants import DB_URI

# print(DB_URI)
client = MongoClient(DB_URI, retryWrites=False)
db = client["audiofy"]
collection = db["files"]



def db_insert(content: str):

    content["_id"] = content["audioFileMetadata"]["id"]
    del content["audioFileMetadata"]["id"]
    print(collection)
    collection.insert_many([content])
    return {"Data Successfully Ingested"}



def db_delete(audioFileType: int, audioFileID: int):

    query = {"_id": int(audioFileID)}
    collection.delete_one(query)
    return {"Data Successfully Deleted"}



def db_update(audioFileType: int, audioFileID: int, content: Dict):

    query = { "_id": int(audioFileID)}
    doc = collection.find_one(query)
    projection_dict = { str("audioFileMetadata."+key): content["audioFileMetadata"][key] for key in content["audioFileMetadata"].keys()}

    if doc["audioFileType"] != content["audioFileType"]:
        projection_dict["audioFileType"]=content["audioFileType"]

    collection.update_one(query, {"$set": projection_dict})

    return {"Data Succesfully Updated"}



def db_search(audioFileType: int, audioFileID: int):

    if audioFileID:
        filter_query = {"_id": int(audioFileID)}
    else:
        filter_query = {"audioFileType": int(audioFileType)}

    related_documents = collection.find(filter_query)
    return list(related_documents)