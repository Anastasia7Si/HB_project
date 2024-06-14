from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from . import schemas, utils


router = APIRouter(
    prefix='/employees',
    tags=['Employees']
)


@router.get(
    '/',
    response_model=List[schemas.Employee],
    status_code=status.HTTP_200_OK
)
async def get_all_employees(
    db: AsyncSession = Depends(get_async_session),
    limit: int = None
):
    """Эндпоинт получения всех сотрудников."""

    employees = await utils.get_all_employees(db, limit)
    return employees


@router.get(
    '/{emloyee_id}',
    response_model=schemas.Employee,
    status_code=status.HTTP_200_OK
)
async def get_employee(
    emloyee_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    """Эндпоинт получения сотрудника."""

    emloyee = await utils.get_employee(
        db, emloyee_id
    )
    return emloyee


@router.get(
    '/subscriptions/{signatory_id}',
    response_model=List[schemas.SubscriptionsBase],
    status_code=status.HTTP_200_OK
)
async def get_all_followers(
    signatory_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    """Эндпоинт получения всех подписчиков одного подписанта."""

    subscriptions = await utils.get_all_followers(db, signatory_id)
    return subscriptions


@router.get(
    '/subscriptions/{follower_id}',
    response_model=List[schemas.SubscriptionsBase],
    status_code=status.HTTP_200_OK
)
async def get_all_subscription(
    follower_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    """Эндпоинт получения всех подписантов одного подписчика."""

    subscriptions = await utils.get_all_follower(db, follower_id)
    return subscriptions


@router.post(
    '/subscriptions/create',
    response_model=schemas.SubscriptionsBase,
    status_code=status.HTTP_201_CREATED
)
async def post_subscription(
    subscribe: schemas.SubscriptionsBase,
    db: AsyncSession = Depends(get_async_session)
):
    """Эндпоинт создания подписки."""

    return await utils.subscription(db, subscribe)


@router.delete(
    '/subscriptions/delete',
    response_model=schemas.SubscriptionsBase,
    status_code=status.HTTP_200_OK
)
async def delete_subscription(
    unsubscribe: schemas.SubscriptionsBase,
    db: AsyncSession = Depends(get_async_session)
):
    """Эндпоинт отмены подписки."""

    return await utils.unsubscribe(db,  unsubscribe)


@router.post(
    '/create',
    response_model=schemas.Employee,
    status_code=status.HTTP_201_CREATED
)
async def create_employee(employee: schemas.EmployeeCreate,
                          db: AsyncSession = Depends(get_async_session)):
    """Эндпоинт создания сотрудника."""

    return await utils.create_employee(db, employee)
