from pydantic import BaseModel, EmailStr, constr, Field
from typing import List, Optional


class Phone(BaseModel):
    value: constr(min_length=11, max_length=12)
    main: bool = False


class Address(BaseModel):
    street: str
    number: int
    complement: str
    neighborhood: str
    city: str
    state: str


class Provider(BaseModel):
    id: Optional[int]
    provider_name: constr(max_length=50)
    email: EmailStr
    phone_numbers: List[Phone] = None
    address: Address


class PaginatedProviders(BaseModel):
    data: List[Provider] = []
    page_size: int
    page: int
    pages: int
