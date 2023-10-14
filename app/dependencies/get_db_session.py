from sqlalchemy.orm import Session
from app.utils.db import db_engine

def get_db_session():
    session = Session(bind=db_engine)
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()