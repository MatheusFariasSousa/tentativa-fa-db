from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schema.product_schema import Product_Schema
from fastapi import HTTPException,status
from db.model import Product,User


class Product_Use_Case:
    def __init__(self,db_session:Session):
        self.db_session = db_session


    def post(self,product:Product_Schema):
        person = self.db_session.query(User).where(User.id==product.user_id).first()
        print(person)
        if not person:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User not found")
        print(person)
        produto = Product(name=product.name,quantity=product.quantity,price=product.price,user_id=product.user_id)
        self.db_session.add(produto)
        self.db_session.commit()

    
    def put(self,product:Product_Schema,id:int):
        new = self.db_session.query(Product).where(Product.id == id).first()
        if not new:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Product invalido")
        new.name = product.name
        new.price = product.price
        new.quantity = product.quantity
        new.user_id = product.user_id
        self.db_session.add(new)
        self.db_session.commit()
        
    def list_product(self):
        list_of_product = self.db_session.query(Product).all()
        for product in list_of_product:
            yield {"id":product.id,"name":product.name,"price":product.price,"quantity":product.quantity}