
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import Float

# declarative base class

class Base(DeclarativeBase):
    pass
    
# an example mapping using the base
class Test(Base):
    __tablename__ = "test"

    x: Mapped[float] = mapped_column(Float(), primary_key=True, nullable=False)
    y: Mapped[float] = mapped_column(Float(), nullable=False)
    delta_y: Mapped[float] = mapped_column(Float(), nullable=False)
    ideal: Mapped[str] = mapped_column(String(), nullable=False)


class Train(Base):
    __tablename__ = "train"

    x: Mapped[float] = mapped_column(Float(), primary_key=True, nullable=False)
    y1: Mapped[float] = mapped_column(Float(), nullable=False)
    y2: Mapped[float] = mapped_column(Float(), nullable=False)
    y3: Mapped[float] = mapped_column(Float(), nullable=False)
    y4: Mapped[float] = mapped_column(Float(), nullable=False)

    def get_field(col: str):
        fields = {}
        fields["y1"]= Train.y1
        fields["y2"]= Train.y2
        fields["y3"]= Train.y3
        fields["y4"]= Train.y4

        return fields.get(col)


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

    def get_field(col: str):
        fields = {}
        fields["y1"]= Ideal.y1
        fields["y2"]= Ideal.y2
        fields["y3"]= Ideal.y3
        fields["y4"]= Ideal.y4
        fields["y5"]= Ideal.y5
        fields["y6"]= Ideal.y6
        fields["y7"]= Ideal.y7
        fields["y8"]= Ideal.y8
        fields["y9"]= Ideal.y9
        fields["y10"]=Ideal.y10
        fields["y11"]=Ideal.y11
        fields["y12"]=Ideal.y12
        fields["y13"]=Ideal.y13
        fields["y14"]=Ideal.y14
        fields["y15"]=Ideal.y15
        fields["y16"]=Ideal.y16
        fields["y17"]=Ideal.y17
        fields["y18"]=Ideal.y18
        fields["y19"]=Ideal.y19
        fields["y20"]=Ideal.y20
        fields["y21"]=Ideal.y21
        fields["y22"]=Ideal.y22
        fields["y23"]=Ideal.y23
        fields["y24"]=Ideal.y24
        fields["y25"]=Ideal.y25
        fields["y26"]=Ideal.y26
        fields["y27"]=Ideal.y27
        fields["y28"]=Ideal.y28
        fields["y29"]=Ideal.y29
        fields["y30"]=Ideal.y30
        fields["y31"]=Ideal.y31
        fields["y32"]=Ideal.y32
        fields["y33"]=Ideal.y33
        fields["y34"]=Ideal.y34
        fields["y35"]=Ideal.y35
        fields["y36"]=Ideal.y36
        fields["y37"]=Ideal.y37
        fields["y38"]=Ideal.y38
        fields["y39"]=Ideal.y39
        fields["y40"]=Ideal.y40
        fields["y41"]=Ideal.y41
        fields["y42"]=Ideal.y42
        fields["y43"]=Ideal.y43
        fields["y44"]=Ideal.y44
        fields["y45"]=Ideal.y45
        fields["y46"]=Ideal.y46
        fields["y47"]=Ideal.y47
        fields["y48"]=Ideal.y48
        fields["y49"]=Ideal.y49
        fields["y50"]=Ideal.y50

        return fields.get(col)


    