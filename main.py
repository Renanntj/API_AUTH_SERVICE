from fastapi import FastAPI
from dotenv import load_dotenv
from passlib.context import CryptContext
from fastapi.security import OAuth2AuthorizationCodeBearer
import os

load_dotenv()
SECRETY_KEY = os.getenv("SECRET_KEY")
app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_schema = OAuth2AuthorizationCodeBearer(tokenUrl=)

from auth_routes import auth_roter

app.include_router(auth_roter)
