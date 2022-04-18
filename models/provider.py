from lib2to3.pytree import Base
from pydantic import BaseModel, EmailStr, constr
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
    provider_name: constr(max_length=50)
    email: EmailStr
    phone: constr(max_length=14)
    address: Address


class PaginatedProviders(BaseModel):
    data: list[Provider] | None
    page_size: int
    page: int
    pages: int
