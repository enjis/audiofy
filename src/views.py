import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
import datetime
import traceback
from typing import Dict
from flask import request
from constants import DB_URI
from bson.objectid import ObjectId
from pymongo import MongoClient
from src.database import db_insert, db_delete, db_update, db_search
from utils.logger import setup_logger, logger




def create_file():
    """
    Add documents to the database
    supports text and pdf
    Only accessible to admin users
    """
    content = request.json
    if type(content) != dict:
        return {"message": "The request is Invalid"}, 400
    
    logger(msg=f'Inserted document {content["audioFileMetadata"]["name"]}', level="info", logfile="info")
    try:
        db_insert(content)
        return {"message": "Document added successfully"}, 200
    except Exception as e:
        full_traceback = traceback.format_exc()
        logger(
            msg=f"EXCEPTION OCCURED IN PYMONGO INSERT{e} {full_traceback}",
            level="error",
            logfile="error",
        )
        return {"message": "Error occured while adding document"}, 500



def delete_file(audioFileType, audioFileID):
    """
    """
    
    logger(msg=f'Deleted document {audioFileID}', level="info", logfile="info")
    try:
        db_delete(audioFileType, audioFileID)
        return {"message": "Document deleted successfully"}, 200
    except Exception as e:
        full_traceback = traceback.format_exc()
        logger(
            msg=f"EXCEPTION OCCURED IN PYMONGO DELETE{e} {full_traceback}",
            level="error",
            logfile="error",
        )
        return {"message": "Error occured while deleting document"}, 500



def update_file(audioFileType, audioFileID):
    """
    """

    content = request.json

    logger(msg=f'Updated document {audioFileID}', level="info", logfile="info")
    try:
        db_update(audioFileType, audioFileID, content)
        return {"message": "Document Updated successfully"}, 200
    except Exception as e:
        full_traceback = traceback.format_exc()
        logger(
            msg=f"EXCEPTION OCCURED WHILE UPDATING {e} {full_traceback}",
            level="error",
            logfile="error",
        )
        return {"message": "Error occured while updating document"}, 500



def get_file(audioFileType, audioFileID):
    """
    """
    logger(msg=f'Search request for {audioFileID}', level="info", logfile="info")
    try:
        response = db_search(audioFileType, audioFileID)
    except Exception as e:
        full_traceback = traceback.format_exc()
        logger(
            msg=f"EXCEPTION OCCURED WHILE UPDATING {e} {full_traceback}",
            level="error",
            logfile="error",
        )
        return {"message": "Error occured while searching document"}, 500

    return { "related_files": response }


def root():
    return {"message": "Audiofy API"}