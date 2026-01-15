from pydantic import BaseModel, Field

class UsersSchema(BaseModel):
    name : str
    email : str
    senha : str = Field(min_length=6, max_length=64)
    
    class Config:
        from_attributes = True