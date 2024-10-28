from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey
from typing import List
from . import Config

Base=Config.BASE

class Order(Base):
    __tablename__ = "orders"


    id:Mapped[int] = mapped_column(primary_key=True)
    product:Mapped[str]
    quantity:Mapped[int]
    price:Mapped[float]

    user: Mapped["User"] = relationship(back_populates="orders")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))