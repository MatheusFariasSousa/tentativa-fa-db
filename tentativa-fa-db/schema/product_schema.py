from pydantic import BaseModel

class Product_Schema(BaseModel):
    name:str
    quantity:int
    price:int
    user_id:int