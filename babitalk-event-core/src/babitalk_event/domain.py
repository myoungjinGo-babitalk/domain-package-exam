from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Event:
    id: int
    title: str
    description: str

class EventRepository(ABC):
    @abstractmethod
    def save(self, event: Event) -> Event:
        pass

class EventService:
    def __init__(self, repository: EventRepository):
        self.repository = repository

    def create_event(self, title:str, description:str) -> Event:
        new_event = Event(
            id=1,
            title=title,
            description=description
        )
        return self.repository.save(new_event)
