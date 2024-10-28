from pydantic import BaseModel,Field,EmailStr
from typing import List


class OrderData(BaseModel):
    product:str
    quantity:int = Field(gt=0)
    price:float = Field(gt=0)
    user_id:int



class UserData(BaseModel):
    name:str
    email:EmailStr

