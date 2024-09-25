from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from routes.deps import get_conection
from use_cases.sale_use_case import Sale_Use_Case  
from schema.sale_schema import Sale_Schema 


rota = APIRouter(prefix="/sale",tags=["Sales"])

@rota.get("/get/{id}")
def get_all(id:int,db_session:Session = Depends(get_conection)):
    uc = Sale_Use_Case(db_session=db_session)
    sale = uc.get_by_id(id=id)
    return sale

@rota.post("/post")
def post_sale(sale:Sale_Schema,db_session:Session = Depends(get_conection)):
    uc = Sale_Use_Case(db_session=db_session)
    sell = uc.comprar(sale=sale)
    return sell

