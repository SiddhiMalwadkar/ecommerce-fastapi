from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class OrderCreate(BaseModel):
    product_id: int