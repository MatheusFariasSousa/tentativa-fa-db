from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schema.product_schema import Product_Schema
from fastapi import HTTPException,status
from db.model import Product


class Product_Use_Case:
    def __init__(self,db_session:Session):
        self.db_session = db_session


    def post(self,product:Product_Schema):
        produto = Product(name=product.name,quantity=product.quantity,price=product.price)
        self.db_session.add(produto)
        self.db_session.commit()

    
    def put(self,product:Product_Schema,id:int):
        new = self.db_session.query(Product).where(Product.id == id).first()
        if not new:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Product invalido")
        new.name = product.name
        new.price = product.price
        new.quantity = product.quantity
        self.db_session.add(new)
        self.db_session.commit()
        