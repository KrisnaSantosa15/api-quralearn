from sqlalchemy.orm import Session
from app.utils.db import db_engine

def get_db_session():
    try:
        session = Session(bind=db_engine)
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()