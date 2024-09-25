from pydantic import BaseModel

class Sale_Schema(BaseModel):
    user_id:int
    product_id:int
    quantity:int
    