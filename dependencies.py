from models import SessionLocal
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from models import Users
from jose import jwt, JWTError  
from config import SECRET_KEY, ALGORITHM
from main import oauth2_schema
def open_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def verify_token(token: str = Depends(oauth2_schema), session: Session = Depends(open_session)):
    try:
        dic = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_user = int(dic.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Access denied")
    user = session.query(Users).filter(Users.id==id_user).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return user


