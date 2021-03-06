import sqlalchemy

from db.init_db import metadata
from models.enums import RoleType


user = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("email", sqlalchemy.String(120), nullable=False, unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(256), nullable=False),
    sqlalchemy.Column("firstname", sqlalchemy.String(126), nullable=False),
    sqlalchemy.Column("lastname", sqlalchemy.String(126), nullable=False),
    sqlalchemy.Column("phone", sqlalchemy.String(50), nullable=True),
    sqlalchemy.Column("iban", sqlalchemy.String(200)),
    sqlalchemy.Column("role", sqlalchemy.Enum(RoleType), nullable=False, server_default=RoleType.buyer.name)
)
