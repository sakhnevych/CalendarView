from datetime import time

from calendar_view.core.config import CalendarConfig
from calendar_view.core.event import Event


class InputData:
    def __init__(self, config: CalendarConfig, events: list):
        self.config = config
        self.events = events


def event(name: str = None, date: str = None, day_of_week: int = None, start_time: str = None, end_time: str = None, interval: str = None):
    return Event(name, date, day_of_week, start_time, end_time, interval)


def validate_config(config: CalendarConfig):
    config.validate()


def validate_event(event: Event, config: CalendarConfig):
    event.validate()

    start_date, end_date = config.get_date_range()
    start_time = time(hour=config.get_hours_range()[0])
    end_hour = config.get_hours_range()[1]
    if not (start_date <= event.get_date(config) <= end_date):
        raise ValueError("Event can't be shown, because it is not in configured date range: {} not in [{}, {}]".format(
            event.get_date(config).strftime('%Y-%m-%d'),
            start_date.strftime('%Y-%m-%d'),
            end_date.strftime('%Y-%m-%d')
        ))
    if event.get_start_time() < start_time:
        raise ValueError("Event can't be shown, because its start is before time range: {} is before {}".format(
            event.get_start_time().strftime('%H:%M'),
            start_time.strftime('%H:%M')
        ))
    if end_hour < 24 and time(hour=end_hour) < event.get_end_time():
        raise ValueError("Event can't be shown, because its end is after time range: {} is before {}".format(
            event.get_end_time().strftime('%H:%M'),
            time(hour=end_hour).strftime('%H:%M')
        ))


def validate_events(events: list, config: CalendarConfig):
    for e in events:
        validate_event(e, config)


def validate_data(data: InputData):
    validate_config(data.config)
    validate_events(data.events, data.config)
