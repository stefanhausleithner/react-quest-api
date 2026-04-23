from pymongo import MongoClient

from app.core.config import MONGO_URI, MONGO_DB_NAME

client = MongoClient(MONGO_URI)
db = client(MONGO_DB_NAME)



def get_lessons_collection():
    return db["lessons"]


def get_quiz_collection():
    return db["quiz_questions"]
