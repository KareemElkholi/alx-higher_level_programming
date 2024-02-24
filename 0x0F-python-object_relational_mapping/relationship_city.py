#!/usr/bin/python3
"""City class module"""
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from relationship_state import State, Base


class City(Base):
    """City class"""
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    state_id: Mapped[int] = mapped_column(ForeignKey(State.id,
                                                     ondelete="CASCADE"))
    state: Mapped[State] = relationship(back_populates="cities")
