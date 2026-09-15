from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str
    price: int
    stock: int

class ResponseProduct(BaseModel):
    name: str
    price: int