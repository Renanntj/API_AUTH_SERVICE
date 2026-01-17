from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

from auth_routes import auth_roter

app.include_router(auth_roter)



@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>API Auth Service</title>
            <style>
                body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #0f172a; color: white; margin: 0; }
                .container { text-align: center; border: 1px solid #1e293b; padding: 2rem; border-radius: 12px; background: #1e293b; }
                a { color: #38bdf8; text-decoration: none; font-weight: bold; }
                .status { color: #4ade80; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🔐 API Auth Service</h1>
                <p>Status: <span class="status">Online</span></p>
                <p>Access <a href="/docs">Documentation Swagger</a> to test the endpoints.</p>
                <br>
                <small>Developed by Renan Alves</small>
            </div>
        </body>
    </html>
    """
