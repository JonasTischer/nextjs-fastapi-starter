"""add oauth_account table

Revision ID: c8f3d9e2a1b4
Revises: b389592974f8
Create Date: 2025-10-29 12:00:00.000000

"""

from alembic import op
import sqlalchemy as sa
from fastapi_users_db_sqlalchemy.generics import GUID

# revision identifiers, used by Alembic.
revision = "c8f3d9e2a1b4"
down_revision = "b389592974f8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create oauth_account table
    op.create_table(
        "oauth_account",
        sa.Column("id", GUID(), nullable=False),
        sa.Column("oauth_name", sa.String(length=100), nullable=False),
        sa.Column("access_token", sa.String(length=1024), nullable=False),
        sa.Column("expires_at", sa.Integer(), nullable=True),
        sa.Column("refresh_token", sa.String(length=1024), nullable=True),
        sa.Column("account_id", sa.String(length=320), nullable=False),
        sa.Column("account_email", sa.String(length=320), nullable=False),
        sa.Column("user_id", GUID(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_oauth_account_account_id"),
        "oauth_account",
        ["account_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_oauth_account_oauth_name"),
        "oauth_account",
        ["oauth_name"],
        unique=False,
    )


def downgrade() -> None:
    # Drop indexes
    op.drop_index(op.f("ix_oauth_account_oauth_name"), table_name="oauth_account")
    op.drop_index(op.f("ix_oauth_account_account_id"), table_name="oauth_account")

    # Drop table
    op.drop_table("oauth_account")
