from dotenv import load_dotenv
import os
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_MINUTES = int(os.getenv("ACCESS_TOKEN_MINUTES"))
ALGORITHM = os.getenv("ALGORITHM")
EMAIL = os.getenv("EMAIL")
PASSWORD_APP = os.getenv("EMAIL_PASS")
CODE_EXP = int(os.getenv("CODE_EXP"))