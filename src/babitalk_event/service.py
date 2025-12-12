from typing import Any, Dict
from babitalk_event.domain import Event
from babitalk_event.repository import EventCommandRepository

class EventService:
    def __init__(self, command_repository: EventCommandRepository):
        self.command_repository = command_repository

    def create_event(self, data: Dict[str, Any]) -> Event:
        new_event = Event(
            id=1,  # Mock ID
            title=data.get("title", "Untitled"),
            description=data.get("description", "")
        )
        
        return self.command_repository.save(new_event)
