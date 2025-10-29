from fastapi import APIRouter

from src.core.config import settings
from .service import (
    fastapi_users,
    auth_backend,
    oauth_auth_backend,
    google_oauth_client,
)
from .schemas import UserRead, UserCreate, UserUpdate

router = APIRouter()

# Include authentication and user management routes
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

# Google OAuth router
router.include_router(
    fastapi_users.get_oauth_router(
        google_oauth_client,
        oauth_auth_backend,  # Use OAuth-specific backend with redirect
        settings.ACCESS_SECRET_KEY,
        associate_by_email=True,  # Auto-link to existing account with same email
        is_verified_by_default=True,  # Trust Google's email verification
    ),
    prefix="/google",
    tags=["auth"],
)
