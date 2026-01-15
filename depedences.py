from models import SessionLocal

def open_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()