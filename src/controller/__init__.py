from pymongo import MongoClient
import os

def get_db(uri=None, dbname=None):
    """
    Retorna um objeto Database do pymongo.
    Usa MONGO_URI e MONGO_DB do ambiente se não passar parâmetros.
    """
    uri = uri or os.environ.get('MONGO_URI', 'mongodb://localhost:27017')
    dbname = dbname or os.environ.get('MONGO_DB', 'biblioteca')
    client = MongoClient(uri)
    return client[dbname]
