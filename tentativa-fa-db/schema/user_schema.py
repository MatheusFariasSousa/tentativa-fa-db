from pydantic import BaseModel

class User_schema(BaseModel):
    name:str
    email:str
    password:str
    cpf_cnpj:str
    is_active:bool

class User_Schema_Output(BaseModel):
    name:str
    email:str
    cpf_cnpj:str
    is_active:bool

class User_Schema_Act(BaseModel):
    is_active:bool

