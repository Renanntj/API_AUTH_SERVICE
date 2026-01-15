from pydantic import BaseModel

class UsersSchema(BaseModel):
    name : str
    email : str
    senha : str
    
    class Config:
        from_atrributes = True