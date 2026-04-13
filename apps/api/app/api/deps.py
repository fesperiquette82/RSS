from app.db.mongo import MongoDB


def get_db():
    return MongoDB.get_db()
