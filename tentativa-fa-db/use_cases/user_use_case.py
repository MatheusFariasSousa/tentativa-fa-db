from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schema.user_schema import User_schema
from fastapi import HTTPException,status
from db.model import User
from passlib.context import CryptContext

crypt =CryptContext(schemes=["sha256_crypt"])



class User_use_cases:
    def __init__(self,db_session:Session):
        self.db_session = db_session


    def post_user(self,user:User_schema):
        person = User(name = user.name,email=user.email,password=crypt.hash(user.password),cpf_cnpj=user.cpf_cnpj,is_active=user.is_active)
        self.db_session.add(person)
        try:
            self.db_session.commit()
            return status.HTTP_200_OK
        except IntegrityError:
            self.db_session.rollback()
            raise HTTPException(detail="Integrity Error",status_code=status.HTTP_401_UNAUTHORIZED)
        
    def get_by_id(self,id:int):
        person = self.db_session.query(User).where(User.id == id).first()
        if not person:
            raise HTTPException(detail="This is a invalid id",status_code=status.HTTP_400_BAD_REQUEST)
        
        return person
    
    
    def get_all(self):
        lista = self.db_session.query(User).all()  
        for person in lista:
            yield {"id":person.id,"name":person.name,"email":person.email,"cpf_cnpj":person.cpf_cnpj,"is_active":person.is_active}

    
    def delete_user(self,id:int):
    
        person = self.db_session.query(User).where(User.id == id).first()
        if not person:
            raise HTTPException(detail="This is a invalid id",status_code=status.HTTP_400_BAD_REQUEST)
        self.db_session.delete(person)
        self.db_session.commit()
        return status.HTTP_200_OK
        
    def put_user(self,id:int,user:User_schema):
        person = self.db_session.query(User).where(User.id == id).first()
        if not person:
            raise HTTPException(detail="This is a invalid id",status_code=status.HTTP_400_BAD_REQUEST)
        person.name=user.name
        person.email = user.email
        person.password = user.password
        person.cpf_cnpj = user.cpf_cnpj
        person.is_active = user.is_active

        self.db_session.add(person)
        
        try:
            self.db_session.commit()
            return person
        except IntegrityError:
            raise HTTPException(detail="Integrity Error",status_code=status.HTTP_401_UNAUTHORIZED)
        
    
            