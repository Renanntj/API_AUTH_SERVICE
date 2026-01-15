from fastapi import APIRouter, Depends, HTTPException
from models import Users
from schemas import UsersSchema
from depedences import open_session
from sqlalchemy.orm import Session
from main import bcrypt_context
auth_roter = APIRouter(prefix="/auth", tags=["auth"])

#solução pro erro de senha:
import hashlib

def hash_password(password: str) -> str:
    return bcrypt_context.hash(password)

@auth_roter.get("/")
async def home():
    return {
        "message": "Welcome to my Auth Service API"
    }
    
@auth_roter.post("/register", status_code=201)
async def create_user_register(user_schema: UsersSchema, session: Session = Depends(open_session)):
    user = session.query(Users).filter(Users.email==user_schema.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Existing user.")
    password_security = hash_password(user_schema.senha)
    new_user = Users(user_schema.email, password_security, user_schema.name)
    session.add(new_user)
    
    try:
        session.commit()
    except Exception:
        session.rollback()
        raise HTTPException(status_code=500, detail="Error creating user.")
    
    return {
        "message": f"User {user_schema.email} successfully registered."
    }
@auth_roter.post("/login")
async def login_user_auth():
    ...