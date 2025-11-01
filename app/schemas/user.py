"""
User-related Pydantic models.
"""
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime


class UserPreferences(BaseModel):
    """User preferences model."""
    wake_time: str = Field(default="07:00", description="Preferred wake time (HH:MM)")
    sleep_time: str = Field(default="23:00", description="Preferred sleep time (HH:MM)")
    work_hours: Dict[str, str] = Field(
        default={"start": "09:00", "end": "17:00"},
        description="Work hours"
    )
    break_frequency: int = Field(default=120, description="Break frequency in minutes")
    focus_areas: List[str] = Field(
        default=["productivity", "health"],
        description="User's focus areas"
    )
    timezone: str = Field(default="UTC", description="User timezone")


class UserProfile(BaseModel):
    """Complete user profile."""
    user_id: str = Field(..., description="Unique user identifier")
    preferences: UserPreferences = Field(default_factory=UserPreferences)
    goals: List[str] = Field(default=[], description="User goals")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user123",
                "preferences": {
                    "wake_time": "07:00",
                    "sleep_time": "23:00",
                    "work_hours": {"start": "09:00", "end": "17:00"},
                    "break_frequency": 120,
                    "focus_areas": ["productivity", "health", "learning"],
                    "timezone": "America/New_York"
                },
                "goals": [
                    "Complete project by end of month",
                    "Exercise 3x per week"
                ]
            }
        }


class Task(BaseModel):
    """Task model."""
    id: str = Field(..., description="Task identifier")
    title: str = Field(..., description="Task title")
    priority: str = Field(default="medium", description="Task priority (low/medium/high)")
    due_date: Optional[str] = None
    estimated_duration: Optional[int] = Field(None, description="Estimated duration in minutes")
    completed: bool = False
    tags: List[str] = Field(default=[], description="Task tags")


class CalendarEvent(BaseModel):
    """Calendar event model."""
    id: str = Field(..., description="Event identifier")
    title: str = Field(..., description="Event title")
    start: str = Field(..., description="Event start time (ISO format)")
    end: str = Field(..., description="Event end time (ISO format)")
    location: Optional[str] = None
    attendees: List[str] = Field(default=[], description="Event attendees")
    description: Optional[str] = None
