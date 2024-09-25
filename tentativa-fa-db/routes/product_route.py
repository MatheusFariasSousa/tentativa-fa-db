from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter,status,HTTPException


from routes.deps import get_conection
from schema.product_schema import Product_Schema

from use_cases.product_use_case import Product_Use_Case


client = APIRouter(prefix="/product",tags=["Product"])

@client.post("/post")
def post_product(product:Product_Schema, db_session:Session=Depends(get_conection)):
    uc = Product_Use_Case(db_session=db_session)
    uc.post(product=product)
    return status.HTTP_200_OK

@client.put("/put/{id}")
def put_prodcut(id:int,product:Product_Schema,db_session:Session=Depends(get_conection)):
    uc = Product_Use_Case(db_session=db_session)
    uc.put(product=product,id=id)
    return status.HTTP_200_OK

@client.get("/get-all")
def get_all(db_session:Session=Depends(get_conection)):
    uc = Product_Use_Case(db_session=db_session)
    return uc.list_product

