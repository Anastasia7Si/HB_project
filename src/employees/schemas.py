from datetime import date
from pydantic import BaseModel, EmailStr


class EmployeeBase(BaseModel):
    """Базовая схема сотрудника компании."""

    id: int
    first_name: str
    second_name: str
    position: str
    date_of_birth: date
    email: EmailStr


class EmployeeCreate(BaseModel):
    """Базовая схема создания сотрудника компании."""

    first_name: str
    second_name: str
    position: str
    date_of_birth: date
    email: EmailStr
    password: str


class Employee(EmployeeBase):

    class Config:
        from_attributes = True


class SubscriptionsBase(BaseModel):
    """Базовая схема подписки/отписки."""

    signatory_id: int
    follower_id: int


class Subscriptions(SubscriptionsBase):

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
