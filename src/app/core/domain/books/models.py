from sqlalchemy import String
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column

from app.connectors.db import Base


class Book(MappedAsDataclass, Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str] = mapped_column(String(255), unique=True)
