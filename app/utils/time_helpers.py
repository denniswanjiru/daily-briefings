"""
Time and date utility functions.
"""
from datetime import datetime, timedelta, time
from typing import Optional, Tuple
import pytz


def get_current_time(timezone: str = "UTC") -> datetime:
    """
    Get current time in specified timezone.

    Args:
        timezone: Timezone string (e.g., "America/New_York")

    Returns:
        Current datetime in specified timezone
    """
    tz = pytz.timezone(timezone)
    return datetime.now(tz)


def parse_time_string(time_str: str) -> time:
    """
    Parse time string in HH:MM format.

    Args:
        time_str: Time string (e.g., "09:30")

    Returns:
        Python time object
    """
    try:
        hour, minute = map(int, time_str.split(':'))
        return time(hour=hour, minute=minute)
    except (ValueError, AttributeError):
        # Default to midnight if parsing fails
        return time(hour=0, minute=0)


def format_time(dt: datetime, format: str = "%I:%M %p") -> str:
    """
    Format datetime as readable time string.

    Args:
        dt: Datetime object
        format: Strftime format string

    Returns:
        Formatted time string
    """
    return dt.strftime(format)


def format_date(dt: datetime, format: str = "%B %d, %Y") -> str:
    """
    Format datetime as readable date string.

    Args:
        dt: Datetime object
        format: Strftime format string

    Returns:
        Formatted date string
    """
    return dt.strftime(format)


def get_time_of_day(dt: Optional[datetime] = None) -> str:
    """
    Get time of day category (morning, afternoon, evening, night).

    Args:
        dt: Datetime object (defaults to now)

    Returns:
        Time of day string
    """
    if dt is None:
        dt = datetime.now()

    hour = dt.hour

    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"


def get_greeting() -> str:
    """
    Get appropriate greeting based on time of day.

    Returns:
        Greeting string
    """
    time_of_day = get_time_of_day()

    greetings = {
        "morning": "Good morning",
        "afternoon": "Good afternoon",
        "evening": "Good evening",
        "night": "Good evening"
    }

    return greetings.get(time_of_day, "Hello")


def calculate_duration(start: datetime, end: datetime) -> int:
    """
    Calculate duration between two datetimes in minutes.

    Args:
        start: Start datetime
        end: End datetime

    Returns:
        Duration in minutes
    """
    delta = end - start
    return int(delta.total_seconds() / 60)


def is_within_work_hours(
    dt: datetime,
    work_start: str = "09:00",
    work_end: str = "17:00"
) -> bool:
    """
    Check if datetime falls within work hours.

    Args:
        dt: Datetime to check
        work_start: Work start time (HH:MM)
        work_end: Work end time (HH:MM)

    Returns:
        True if within work hours
    """
    start_time = parse_time_string(work_start)
    end_time = parse_time_string(work_end)
    current_time = dt.time()

    return start_time <= current_time <= end_time


def get_next_break_time(
    current_time: datetime,
    break_frequency: int = 120
) -> datetime:
    """
    Calculate next suggested break time.

    Args:
        current_time: Current datetime
        break_frequency: Break frequency in minutes

    Returns:
        Next break datetime
    """
    return current_time + timedelta(minutes=break_frequency)


def format_relative_time(dt: datetime) -> str:
    """
    Format datetime as relative time (e.g., "in 2 hours", "5 minutes ago").

    Args:
        dt: Datetime object

    Returns:
        Relative time string
    """
    now = datetime.now(dt.tzinfo) if dt.tzinfo else datetime.now()
    delta = dt - now

    if delta.total_seconds() < 0:
        # Past
        delta = -delta
        suffix = "ago"
    else:
        # Future
        suffix = "from now"

    seconds = int(delta.total_seconds())

    if seconds < 60:
        return f"{seconds} second{'s' if seconds != 1 else ''} {suffix}"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes} minute{'s' if minutes != 1 else ''} {suffix}"
    elif seconds < 86400:
        hours = seconds // 3600
        return f"{hours} hour{'s' if hours != 1 else ''} {suffix}"
    else:
        days = seconds // 86400
        return f"{days} day{'s' if days != 1 else ''} {suffix}"


def get_day_boundaries(
    date: Optional[datetime] = None,
    timezone: str = "UTC"
) -> Tuple[datetime, datetime]:
    """
    Get start and end of day boundaries.

    Args:
        date: Date to get boundaries for (defaults to today)
        timezone: Timezone string

    Returns:
        Tuple of (start_of_day, end_of_day)
    """
    tz = pytz.timezone(timezone)

    if date is None:
        date = datetime.now(tz)

    start_of_day = date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = date.replace(hour=23, minute=59, second=59, microsecond=999999)

    return start_of_day, end_of_day
