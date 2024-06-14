from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


async def get_all_employees(db: AsyncSession,
                            limit: int):
    """Функция получения всех сотрудников."""

    stmt = select(models.Employee).limit(limit)
    result = await db.execute(stmt)
    await db.commit()
    return result.unique().scalars().all()


async def get_employee(db: AsyncSession,
                       emloyee_id: int):
    """Функция получения одного сотрудника."""

    stmt = select(models.Employee).filter(models.Employee.id == emloyee_id)
    result = await db.execute(stmt)
    return result.scalars().first()


async def get_all_follower(db: AsyncSession,
                           signatory_id: int):
    """Функция получения всех подписчиков одного подписанта."""

    stmt = select(models.Subscriptions).filter(
        models.Subscriptions.signatory_id == signatory_id
        )
    result = await db.execute(stmt)
    return result.unique().scalars().all()


async def get_all_subscription(db: AsyncSession,
                               follower_id: int):
    """Функция получения всех подписантов одного подписчика."""

    stmt = select(models.Subscriptions).filter(
        models.Subscriptions.follower_id == follower_id
        )
    result = await db.execute(stmt)
    return result.unique().scalars().all()


async def subscription(db: AsyncSession,
                       subscribe: schemas.SubscriptionsBase):
    """Функция подписки на уведомления о дне рождения."""

    subscribe_hb = models.Subscriptions(**subscribe.model_dump())
    db.add(subscribe_hb)
    db.commit
    return subscribe_hb


async def unsubscribe(db: AsyncSession,
                      unsubscribe: schemas.SubscriptionsBase):
    """Функция отписки на уведомления о дне рождения."""

    subscribe = await db.execute(select(models.Subscriptions).filter(
        models.Subscriptions.signatory_id == unsubscribe.signatory_id,
        models.Subscriptions.follower_id == unsubscribe.follower_id))
    db.delete(subscribe.scalar())
    db.commit()
    return unsubscribe


async def create_employee(db: AsyncSession,
                          employee: schemas.EmployeeBase):
    """Функция создания пользователя."""

    company_employee = models.Employee(**employee.model_dump())
    db.add(company_employee)
    await db.commit()
    return company_employee


def verify_password(plain_password: str, hashed_password: str):
    return plain_password == hashed_password
