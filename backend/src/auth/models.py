from fastapi_users.db import (
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyBaseOAuthAccountTableUUID,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from typing import List


class Base(DeclarativeBase):
    pass


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    """OAuth account for third-party authentication (Google, GitHub, etc.)"""

    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    """User model with OAuth support"""

    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined"
    )
