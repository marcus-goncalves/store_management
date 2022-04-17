from lib2to3.pytree import Base
from pydantic import BaseModel, EmailStr
from dataclasses import dataclass


@dataclass
class Address:
    street: str
    number: int
    complement: str | int
    neighborhood: str
    city: str
    state: str


class Provider(BaseModel):
    provider_name: str
    email: EmailStr
    phone: int
    address: Address
