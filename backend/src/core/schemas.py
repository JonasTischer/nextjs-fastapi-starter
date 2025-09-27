"""Base Pydantic models shared by the application."""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, ConfigDict


def _datetime_to_iso(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))
    return dt.strftime("%Y-%m-%dT%H:%M:%S%z")


class AppBaseModel(BaseModel):
    """Custom base model enforcing consistent serialization."""

    model_config = ConfigDict(
        json_encoders={datetime: _datetime_to_iso}, populate_by_name=True
    )

    def serializable_dict(self, **kwargs):
        return jsonable_encoder(self.model_dump(**kwargs))
