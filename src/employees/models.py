from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base


class Employee(Base):
    """Модель сотрудника компании."""

    __tablename__ = 'employee'

    id = Column(
        Integer,
        primary_key=True
    )
    first_name = Column(
        String(15)
    )
    second_name = Column(
        String(30)
    )
    position = Column(
        String(50)
    )
    date_of_birth = Column(
        Date()
    )
    email = Column(
        String(50),
        index=True,
        unique=True
    )
    password = Column(
        String(15)
    )
    sent_subscriptions = relationship(
        'Subscriptions',
        foreign_keys='Subscriptions.signatory_id',
        overlaps='sent_subscriptions'
    )
    received_subscriptions = relationship(
        'Subscriptions',
        foreign_keys='Subscriptions.follower_id',
        overlaps='received_subscriptions'
    )


class Subscriptions(Base):
    """Модель подписок."""

    __tablename__ = 'subscriptions'

    id = Column(
        Integer,
        primary_key=True
    )
    signatory_id = Column(
        Integer,
        ForeignKey('employee.id')
    )
    follower_id = Column(
        Integer,
        ForeignKey('employee.id')
    )
    signatory = relationship(
        'Employee',
        foreign_keys=[signatory_id],
        backref='sent_subs_records',
        overlaps='sent_subscriptions'
    )
    follower = relationship(
        'Employee',
        foreign_keys=[follower_id],
        backref='received_subs_records',
        overlaps='received_subscriptions'
    )
