"""BabiTalk Event Core Package

This package provides domain models, repositories, and services for event management.
"""

from babitalk_event.domain import Event
from babitalk_event.repository import EventCommandRepository, EventQueryRepository
from babitalk_event.service import EventService

__version__ = "0.1.0"

__all__ = [
    "Event",
    "EventCommandRepository",
    "EventQueryRepository",
    "EventService",
]
