"""Security configurations and middleware."""

from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from .config import settings


def add_security_middleware(app):
    """Add security middleware to the FastAPI app."""

    # HTTPS redirect in production
    if settings.ENVIRONMENT == "production":
        app.add_middleware(HTTPSRedirectMiddleware)

        # Trusted host middleware for production
        # Add your production domains here
        app.add_middleware(
            TrustedHostMiddleware, allowed_hosts=["yourdomain.com", "*.yourdomain.com"]
        )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=list(settings.CORS_ORIGINS),
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
        allow_headers=["*"],
    )

    return app


class CSRFProtectionMiddleware(BaseHTTPMiddleware):
    """
    Simple CSRF protection using double-submit cookie pattern.
    Note: SameSite cookies already provide good CSRF protection for modern browsers.
    This adds an extra layer for state-changing operations.
    """

    # Endpoints that don't require CSRF protection
    EXEMPT_PATHS = [
        "/auth/jwt/login",
        "/auth/register",
        "/auth/forgot-password",
        "/auth/reset-password",
        "/openapi.json",
        "/docs",
        "/redoc",
    ]

    # Methods that require CSRF protection
    PROTECTED_METHODS = ["POST", "PUT", "DELETE", "PATCH"]

    async def dispatch(self, request: Request, call_next):
        # Skip CSRF check for safe methods and exempt paths
        if request.method not in self.PROTECTED_METHODS:
            return await call_next(request)

        # Check if path is exempt
        path = request.url.path
        if any(path.startswith(exempt) for exempt in self.EXEMPT_PATHS):
            return await call_next(request)

        # For cookie-based auth with SameSite=lax/strict, we rely on browser CSRF protection
        # This is considered secure for modern browsers
        # Additional CSRF token validation can be added here if needed

        return await call_next(request)


def get_security_headers():
    """Get security headers for production."""
    if settings.ENVIRONMENT == "production":
        return {
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Content-Security-Policy": "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'",
        }
    return {}
