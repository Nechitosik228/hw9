from sqlalchemy.orm import Mapped,mapped_column,relationship
from typing import List
from . import Config

Base=Config.BASE

class User(Base):
    __tablename__ = "users"


    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    email:Mapped[str]
    orders:Mapped[List["Order"]] = relationship(back_populates="user")