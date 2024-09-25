from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from db.model import User
from routes.deps import get_conection
from schema.user_schema import User_schema,User_Schema_Output,User_Schema_Act
from schema.token_schema import Token
from use_cases.user_use_case import User_use_cases
from passlib.context import CryptContext
from security.user_security import create_access_token,get_current_user


crypt =CryptContext(schemes=["sha256_crypt"])

router = APIRouter(prefix="/user",tags=["User"])


@router.get("/get/{id}",response_model=User_Schema_Output)
def get_by_id(id:int,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    person = uc.get_by_id(id=id)
    return person

@router.get("/get")
def get_all(db_session:Session = Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    return uc.get_all()

@router.post("/post")
def post_user(user:User_schema,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    uc.post_user(user=user)
    return status.HTTP_200_OK

@router.delete("/delete/{id}")
def delete(id:int,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    uc.delete_user(id=id)
    return status.HTTP_200_OK
    

@router.put("/put/{id}",response_model=User_Schema_Output)
def put(id:int,user:User_schema,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    return uc.put_user(id=id,user=user)

@router.put("/put_act/{id}",response_model=User_Schema_Output)
def put_act(id:int,db_session:Session=Depends(get_conection)):
    
    user = db_session.query(User).where(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if user.is_active:
        user.is_active = False
        db_session.add(user)
        db_session.commit()
        return user
    user.is_active = True
    db_session.add(user)
    db_session.commit()
    return user
    

    
    
    

    

    

"""@router.post("/token",response_model=Token,tags=["Token"])
def user_token(forms:OAuth2PasswordRequestForm = Depends(),db_session:Session=Depends(get_conection)):
    user = db_session.query(User).where(User.name==forms.username).first()
    if not user or not crypt.verify(forms.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Usuario ou senha incorreto")
    access_token = create_access_token(data={"sub":user.name})

    return {"access_token": access_token,"token_type":"bearer"}"""


'''@router.get("/get_you")
def get_you(db_session:Session=Depends(get_conection),current_user:User = Depends(get_current_user)):
    person = db_session.query(User).where(User.name==current_user.name).first()
    return person'''
