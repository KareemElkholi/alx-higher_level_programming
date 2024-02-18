#!/usr/bin/python3
"""State class module"""
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    """Base class"""
    pass


class State(Base):
    """State class"""
    __tablename__ = "states"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
