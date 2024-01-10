from icalendar import Calendar, Event
from datetime import datetime
import pytz


cal = Calendar()


eastern = pytz.timezone('US/Eastern')


events = [
   {"summary": "Team Meeting", "date": "2024-06-15 10:00"},
]


for event_info in events:
    event = Event()
    event.add('summary', event_info["summary"])
    event_date = datetime.strptime(event_info["date"], "%Y-%m-%d %H:%M" if ":" in event_info["date"] else "%Y-%m-%d")
    event_date = eastern.localize(event_date)
    event.add('dtstart', event_date)
    cal.add_component(event)


with open('my_calendar.ics', 'wb') as f:
    f.write(cal.to_ical())
