import enum

from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()

class UniversityEnum(enum.Enum):
    UPF = "UPF"
    ULBRA = "ULBRA"


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome_completo: Mapped[str]
    universidade: Mapped[UniversityEnum] = mapped_column(SQLEnum(UniversityEnum, name="university_enum"))
    matricula: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
