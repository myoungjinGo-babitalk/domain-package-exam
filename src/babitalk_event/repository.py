from abc import ABC, abstractmethod
from typing import List, Optional
from babitalk_event.domain import Event

class EventCommandRepository(ABC):
    @abstractmethod
    def save(self, event: Event) -> Event:
        pass

class EventQueryRepository(ABC):
    @abstractmethod
    def find_by_id(self, event_id: int) -> Optional[Event]:
        pass
    
    @abstractmethod
    def find_all(self) -> List[Event]:
        pass
