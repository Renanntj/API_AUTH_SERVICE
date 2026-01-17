from pydantic import BaseModel, Field

class UsersSchema(BaseModel):
    name : str
    email : str
    senha : str = Field(min_length=6, max_length=64)
    
    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str
    
    class Config:
        from_attributes = True
        
class RecoverPasswordRequest(BaseModel):
    email: str
    
    class Config:
        from_attributes = True
        
class VerifyCodeRequest(BaseModel):
    email: str
    code: str

    class Config:
        from_attributes = True
        
class ResetPasswordRequest(BaseModel):
    email: str
    code: str
    new_password: str
    
    class Config:
        from_attributes = True