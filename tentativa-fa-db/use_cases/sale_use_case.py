from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schema.product_schema import Product_Schema
from schema.sale_schema import Sale_Schema  
from fastapi import HTTPException,status
from db.model import Product,User,Sales

class Sale_Use_Case:
    def __init__(self,db_session:Session):
        self.db_session = db_session

    def comprar(self,sale:Sale_Schema):
        quant = self.db_session.query(Product).where(Product.id == sale.product_id).where(User.id == sale.user_id).first()
        if not quant:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid product or user id")
        if quant.quantity<sale.quantity:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="there is not enough product avaible in stock")
        quant.quantity -= sale.quantity
        price = sale.quantity * quant.price
        self.db_session.add(quant)
        try:
            self.db_session.commit()
        except:
            HTTPException(detail="product put error")
        sell = Sales(sale.user_id,sale.product_id,sale.quantity,price)
        self.db_session.add(sell)
        try:
            self.db_session.commit()
        except:
            HTTPException(detail="sell post error")
    
    def get_by_id(self,id:int):
        sale = self.db_session.query(Sales).where(Sales.id==id).first()
        if not sale:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid id")
        return sale


        


