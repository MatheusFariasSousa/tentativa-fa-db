from sqlalchemy.orm import registry,Mapped,mapped_column
from db.connection import engine
<<<<<<< HEAD
from sqlalchemy import ForeignKey   
=======
from sqlalchemy import ForeignKey
>>>>>>> 917240fe7ed23c246a5cea183a217d046661eb9c

table_registry = registry()

@table_registry.mapped_as_dataclass
class User():
    __tablename__="User"
    
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True,init=False)    
    name:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False)
    password:Mapped[str] = mapped_column(nullable=False)
    cpf_cnpj:Mapped[str] = mapped_column(nullable=True)
    is_active:Mapped[bool] = mapped_column(nullable=False,default=True)

@table_registry.mapped_as_dataclass
class Product():
    __tablename__="Product"

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True,init=False)
    name:Mapped[str] = mapped_column(nullable=False)
    quantity:Mapped[int] = mapped_column(nullable=False)
    price:Mapped[int]=mapped_column(nullable=False)
<<<<<<< HEAD
    user_id:Mapped[int]=mapped_column(ForeignKey("User.id"),nullable=True)

@table_registry.mapped_as_dataclass
class Sales():
    __tablename__="Sales"

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True,init=False)
    user_id:Mapped[int]=mapped_column(ForeignKey("User.id"),nullable=True)
    product_id:Mapped[int]=mapped_column(ForeignKey ("Product.id"),nullable=True)
    quantity:Mapped[int]=mapped_column(nullable=False)
    price:Mapped[int]=mapped_column(nullable=False)
     
=======
    user_id:Mapped[int]=mapped_column(ForeignKey("User.id"))

@table_registry.mapped_as_dataclass
class Sale():
    __tablename__="Sale"

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True,init=False)
    user_id:Mapped[int]=mapped_column(ForeignKey("User.id"))
    product_id:Mapped[int]=mapped_column(ForeignKey("Product.id"))
    quantity:Mapped[int] = mapped_column(nullable=False)
    price:Mapped[int]=mapped_column(nullable=False)


>>>>>>> 917240fe7ed23c246a5cea183a217d046661eb9c





table_registry.metadata.create_all(engine)
