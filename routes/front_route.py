from fastapi import APIRouter,Form,Depends,Response,status,HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from sqlalchemy.orm import Session
from typing import List
from routes.deps import get_conection
from use_cases.user_use_case import User_use_cases
from passlib.context import CryptContext
from schema.user_schema import User_schema,User_Schema_Front
from db.model import User

front_router = APIRouter(prefix="/front",tags=["Front"])

crypt =CryptContext(schemes=["sha256_crypt"])

templates = Jinja2Templates(directory="templates")

@front_router.get("/")
def read_front(request:Request):
    return templates.TemplateResponse(request=request,name="index.html")

@front_router.get("/sucesso")
def success_page(request: Request):
    return templates.TemplateResponse("sucesso.html", {"request": request})

@front_router.post("/result-form")
def post_front(db_session:Session = Depends(get_conection),nome:str=Form(...),cpf:str=Form(...),senha:str=Form(...),email:str=Form(...)):
    person = User_schema(name=nome,email=email,password=senha,cpf_cnpj=cpf,is_active=True)
    uc = User_use_cases(db_session=db_session)
    uc.post_user(person)
    print("!")
    return RedirectResponse(url="/front/sucesso", status_code=303)

@front_router.get("/users-page")
def get_page(request:Request):
    return templates.TemplateResponse("users.html",{"request":request})

@front_router.get("/users_list", response_model=List[User_Schema_Front])
def get_users(db_session: Session = Depends(get_conection)):
    users = db_session.query(User).all()
    return users 

@front_router.post("/put-user")
def put_user(db_session:Session = Depends(get_conection),name:str=Form(...),id:int=Form(...),password:str=Form(...),email:str=Form(...)):
    person = db_session.query(User).where(User.id == id).first()
    print(1)
    person.email = email
    person.name = name
    person.password = password
    db_session.add(person)
    try:
        db_session.commit()
        return RedirectResponse(url="/front/users-page", status_code=303)

    except:
        return "Erro!"


    
    

