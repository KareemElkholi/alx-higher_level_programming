#!/usr/bin/python3
"""City class module"""
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from model_state import State


class Base(DeclarativeBase):
    """Base class"""
    pass


class City(Base):
    """City class"""
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    state_id: Mapped[int] = mapped_column(ForeignKey(State.id))
