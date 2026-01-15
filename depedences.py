from sqlalchemy.orm import Session, sessionmaker
from models import DATABASE_URL

def open_session():
    try:
        Session = sessionmaker(bind=DATABASE_URL)
        session = Session()
        yield session
    finally:
        session.close()