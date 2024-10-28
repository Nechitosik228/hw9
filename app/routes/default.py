from ..schemas import OrderData,UserData
from db import Config,Order,User
from sqlalchemy import select
from fastapi import HTTPException
from pydantic import EmailStr
from . import app



Session=Config.SESSION


@app.post("/user")
def create_user(data:UserData):
    with Session.begin() as session:
        user=User(**data.model_dump())
        session.add(user)
        return "Succesfully created"


@app.post("/order")
def create_order(data:OrderData):
    with Session.begin() as session:
        order=Order(**data.model_dump())
        session.add(order)
        return "Succesfully created"


@app.get("/order")
def get_order(email:EmailStr):
    with Session() as session:
        user=session.scalar(select(User).where(User.email==email))
        if not user:
            raise HTTPException(status_code=404,detail="Not found")
        orders=session.scalars(select(Order).where(Order.user_id==user.id)).all()
        return {"name":user.name,
                "orders":orders}