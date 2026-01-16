from fastapi import APIRouter, Depends, HTTPException
from models import Users
from dependencies import open_session, verify_token
from main import bcrypt_context
from config import ALGORITHM, ACCESS_TOKEN_MINUTES, SECRET_KEY
from schemas import UsersSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm

auth_roter = APIRouter(prefix="/auth", tags=["auth"])


def hash_password(password: str) -> str:
    return bcrypt_context.hash(password)

def auth_user(email, password, session):
    user = session.query(Users).filter(Users.email==email).first()
    if not user:
        return False
    elif not bcrypt_context.verify(password, user.senha):
        return False
    return user

def create_token(id_user, duration_token=timedelta(minutes=ACCESS_TOKEN_MINUTES)):
    date_exp = datetime.now(timezone.utc) + duration_token
    dic = {"sub": str(id_user), "exp": date_exp}
    jwt_code = jwt.encode(dic, SECRET_KEY, ALGORITHM)
    return jwt_code
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
async def login_user_auth(user_schema: LoginSchema, session: Session = Depends(open_session)):
    user = auth_user(user_schema.email, user_schema.senha, session)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password.")
    else:
        access_token = create_token(user.id)
        refresh_token = create_token(user.id, duration_token=timedelta(days=7))
        return {"access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "Bearer"
        }
        
@auth_roter.post("/login-form")
async def login_user_auth(dados_form : OAuth2PasswordRequestForm = Depends(), session: Session = Depends(open_session)):
    user = auth_user(dados_form.username, dados_form.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password.")
    else:
        access_token = create_token(user.id)
        return {"access_token": access_token,
                "token_type": "Bearer"
                }
 
@auth_roter.get("/refresh")
async def refresh_roter_auth(user: Session = Depends(verify_token)):
    access_token = create_token(user.id)
    return {"access_token": access_token,
            "token_type": "Bearer"
        }