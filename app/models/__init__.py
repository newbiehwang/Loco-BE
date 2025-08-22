# app/models/__init__.py
from .user import User
from .trip import Trip
from .region import Region
from .message import Message
from .loco import Loco

__all__ = ["User", "Trip", "Region", "Message", "Loco"]