# Here you can practice class
from typing import TypedDict
from collection import defaultdict


class Event(TypedDict):
    url: str
    visitorId: str
    timestamp: int


class Input(TypedDict):
    events: list[Event]


class Session(TypedDict):
    duration: int
    pages: list[str]
    startTime: int


class Output(TypedDict):
    sessionsByUser: list[Session]


class UserSession:
    def __init__(self, input_data: Input) -> None:
        self.data = input_data

    def print(self):
        print("Printed data: ", self.map_visitor_to_events())

    def generate(self) -> Output:
        visitor_events_map = self.map_visitor_to_events()

        return self.split_visitor_events_to_sessions(visitor_events_map)

    def map_visitor_to_events(self):
        visitor_events_map = defaultdict(list)
        for event in input["events"]:
            visitor_events_map[event["visitorId"]].append((event["timestamp"], event["url"]))

    def split_visitor_events_to_sessions(self, visitor_events_map):
        pass


def main():
    session = UserSession(input_data=input)
    session.print()


if __name__ == "__main__":
    main()

input: Input = {
    "events": [
        {
            "url": "/pages/a-big-river",
            "visitorId": "d1177368-2310-11e8-9e2a-9b860a0d9039",
            "timestamp": 1512754583000
        },
        {
            "url": "/pages/a-small-dog",
            "visitorId": "d1177368-2310-11e8-9e2a-9b860a0d9039",
            "timestamp": 1512754631000
        },
        {
            "url": "/pages/a-big-talk",
            "visitorId": "f877b96c-9969-4abc-bbe2-54b17d030f8b",
            "timestamp": 1512709065294
        },
        {
            "url": "/pages/a-sad-story",
            "visitorId": "f877b96c-9969-4abc-bbe2-54b17d030f8b",
            "timestamp": 1512711000000
        },
        {
            "url": "/pages/a-big-river",
            "visitorId": "d1177368-2310-11e8-9e2a-9b860a0d9039",
            "timestamp": 1512754436000
        },
        {
            "url": "/pages/a-sad-story",
            "visitorId": "f877b96c-9969-4abc-bbe2-54b17d030f8b",
            "timestamp": 1512709024000
        }
    ]
}
