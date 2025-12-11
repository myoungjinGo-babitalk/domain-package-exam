import sys
import os
from babitalk_event.domain import EventService, Event, EventRepository


# 레포지토리 구현체 구현
class MockEventRepository(EventRepository):
    def save(self, event: Event) -> Event:
        event.id = 123
        return event

def main():
    event_repository = MockEventRepository()
    # 구현체 주입
    event_service = EventService(event_repository)
    event = event_service.create_event("이벤트_타이틀", "이벤트_설명")
    print(event)

if __name__ == "__main__":
    main()
