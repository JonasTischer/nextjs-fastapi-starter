from fastapi import FastAPI
from fastapi_pagination import add_pagination
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.shared.utils import simple_generate_unique_route_id
from src.core.config import settings
from src.core.security import CSRFProtectionMiddleware

app = FastAPI(
    generate_unique_id_function=simple_generate_unique_route_id,
    openapi_url=settings.OPENAPI_URL,
)

# Middleware for CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add CSRF protection middleware
# Note: With SameSite=lax/strict cookies, modern browsers already provide CSRF protection
app.add_middleware(CSRFProtectionMiddleware)

# Include routers
app.include_router(auth_router, prefix="/auth")

add_pagination(app)
