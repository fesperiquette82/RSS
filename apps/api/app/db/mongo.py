import logging

from pymongo import MongoClient
from pymongo.errors import PyMongoError

from app.core.config import get_settings


class MongoDB:
    client: MongoClient | None = None

    @classmethod
    def connect(cls) -> None:
        settings = get_settings()
        try:
            cls.client = MongoClient(settings.mongodb_url, serverSelectionTimeoutMS=1500)
            cls.client.admin.command("ping")
        except PyMongoError:
            logging.getLogger(__name__).warning("MongoDB unavailable at startup; DB routes may fail.")
            cls.client = None

    @classmethod
    def disconnect(cls) -> None:
        if cls.client:
            cls.client.close()
            cls.client = None

    @classmethod
    def get_db(cls):
        if cls.client is None:
            cls.connect()
        settings = get_settings()
        return cls.client[settings.db_name]
