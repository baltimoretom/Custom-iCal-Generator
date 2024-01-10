# Calendar Event Script

## Overview

This Python script creates an iCal file (`my_calendar.ics`) containing specified events. It uses `icalendar` and `pytz` libraries for iCal formatting and timezone management. This script is suitable for generating a custom calendar file importable into Google Calendar, Apple Calendar, Microsoft Outlook, and other calendar applications.

## Requirements

- Python 3.x
- `icalendar` library
- `pytz` library

Install the required libraries using pip:

````bash
pip install icalendar pytz


## Usage

1. **Modify the Events List**: The script includes an `events` list. Each event is a dictionary with `summary` (the title or description) and `date` (the event's date and time). Modify this list with your events.

   Example event format:

   ```python
   {"summary": "Event Title", "date": "YYYY-MM-DD HH:MM"}
````

Use `YYYY-MM-DD` for events without a specific time.

2. **Run the Script**: Execute the script in your Python environment:

   ```bash
   python path_to_script.py
   ```

   This generates an `my_calendar.ics` file in the script's directory.

3. **Import the .ics File**: Import this file into your calendar application.

## Script Breakdown

- **Imports**: The script begins with necessary module imports.
- **Calendar Initialization**: A new calendar object is created.
- **Timezone Setting**: Sets the timezone to Eastern Time (US/Eastern).
- **Event Creation**: Processes and adds each event in `events` to the calendar.
- **File Writing**: Writes the calendar to an .ics file (`my_calendar.ics`).

## Note

The script uses Eastern Time by default. Change the `eastern` variable for a different timezone.

---

Customize this script as needed. For issues or questions, refer to `icalendar` and `pytz` documentation or seek Python programming community support.
