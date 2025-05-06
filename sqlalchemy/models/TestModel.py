import BaseModel

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class TestModel(BaseModel):
    __tablename__ = "test"

    age: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(20))