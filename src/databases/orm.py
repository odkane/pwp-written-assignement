from dataclasses import dataclass
from pathlib import Path
import pandas as pd
import sqlalchemy as orm
from sqlalchemy import Engine, create_engine, func, select, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.types import Float


# declarative base class

class Base(DeclarativeBase):
    pass
    
# an example mapping using the base
class Test(Base):
    __tablename__ = "test"

    x: Mapped[float] = mapped_column(Float(), primary_key=True, nullable=False)
    y: Mapped[float] = mapped_column(Float(), nullable=False)
    


class Train(Base):
    __tablename__ = "train"

    x: Mapped[float] = mapped_column(Float(), primary_key=True, nullable=False)
    y1: Mapped[float] = mapped_column(Float(), nullable=False)
    y2: Mapped[float] = mapped_column(Float(), nullable=False)
    y3: Mapped[float] = mapped_column(Float(), nullable=False)
    y4: Mapped[float] = mapped_column(Float(), nullable=False)


class Ideal(Base):
    __tablename__ = "ideal"

    x: Mapped[float] = mapped_column(Float(), primary_key=True, nullable=False)
    y1: Mapped[float] = mapped_column(Float(), nullable=False)
    y2: Mapped[float] = mapped_column(Float(), nullable=False)
    y3: Mapped[float] = mapped_column(Float(), nullable=False)
    y4: Mapped[float] = mapped_column(Float(), nullable=False)
    y5: Mapped[float] = mapped_column(Float(), nullable=False)
    y6: Mapped[float] = mapped_column(Float(), nullable=False)
    y7: Mapped[float] = mapped_column(Float(), nullable=False)
    y8: Mapped[float] = mapped_column(Float(), nullable=False)
    y9: Mapped[float] = mapped_column(Float(), nullable=False)
    y10: Mapped[float] = mapped_column(Float(), nullable=False)
    y11: Mapped[float] = mapped_column(Float(), nullable=False)
    y12: Mapped[float] = mapped_column(Float(), nullable=False)
    y13: Mapped[float] = mapped_column(Float(), nullable=False)
    y14: Mapped[float] = mapped_column(Float(), nullable=False)
    y15: Mapped[float] = mapped_column(Float(), nullable=False)
    y16: Mapped[float] = mapped_column(Float(), nullable=False)
    y17: Mapped[float] = mapped_column(Float(), nullable=False)
    y18: Mapped[float] = mapped_column(Float(), nullable=False)
    y19: Mapped[float] = mapped_column(Float(), nullable=False)
    y20: Mapped[float] = mapped_column(Float(), nullable=False)
    y21: Mapped[float] = mapped_column(Float(), nullable=False)
    y22: Mapped[float] = mapped_column(Float(), nullable=False)
    y23: Mapped[float] = mapped_column(Float(), nullable=False)
    y24: Mapped[float] = mapped_column(Float(), nullable=False)
    y25: Mapped[float] = mapped_column(Float(), nullable=False)
    y26: Mapped[float] = mapped_column(Float(), nullable=False)
    y27: Mapped[float] = mapped_column(Float(), nullable=False)
    y28: Mapped[float] = mapped_column(Float(), nullable=False)
    y29: Mapped[float] = mapped_column(Float(), nullable=False)
    y30: Mapped[float] = mapped_column(Float(), nullable=False)
    y31: Mapped[float] = mapped_column(Float(), nullable=False)
    y32: Mapped[float] = mapped_column(Float(), nullable=False)
    y33: Mapped[float] = mapped_column(Float(), nullable=False)
    y34: Mapped[float] = mapped_column(Float(), nullable=False)
    y35: Mapped[float] = mapped_column(Float(), nullable=False)
    y36: Mapped[float] = mapped_column(Float(), nullable=False)
    y37: Mapped[float] = mapped_column(Float(), nullable=False)
    y38: Mapped[float] = mapped_column(Float(), nullable=False)
    y39: Mapped[float] = mapped_column(Float(), nullable=False)
    y40: Mapped[float] = mapped_column(Float(), nullable=False)
    y41: Mapped[float] = mapped_column(Float(), nullable=False)
    y42: Mapped[float] = mapped_column(Float(), nullable=False)
    y43: Mapped[float] = mapped_column(Float(), nullable=False)
    y44: Mapped[float] = mapped_column(Float(), nullable=False)
    y45: Mapped[float] = mapped_column(Float(), nullable=False)
    y46: Mapped[float] = mapped_column(Float(), nullable=False)
    y47: Mapped[float] = mapped_column(Float(), nullable=False)
    y48: Mapped[float] = mapped_column(Float(), nullable=False)
    y49: Mapped[float] = mapped_column(Float(), nullable=False)
    y50: Mapped[float] = mapped_column(Float(), nullable=False)




    