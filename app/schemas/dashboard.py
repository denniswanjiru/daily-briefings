"""
Dashboard and briefing-related Pydantic models.
"""
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime

from app.schemas.user import UserPreferences, CalendarEvent, Task


class BriefingRequest(BaseModel):
    """Request model for generating a briefing."""
    user_id: str = Field(..., description="Unique user identifier")
    preferences: Optional[UserPreferences] = None
    context: Dict[str, Any] = Field(
        default={},
        description="Additional context for briefing generation"
    )
    include_calendar: bool = Field(default=True, description="Include calendar events")
    include_tasks: bool = Field(default=True, description="Include task list")

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user123",
                "context": {
                    "mood": "energetic",
                    "focus_area": "productivity"
                },
                "include_calendar": True,
                "include_tasks": True
            }
        }


class PlannerOutput(BaseModel):
    """Output from the planner agent."""
    daily_schedule: List[Dict[str, Any]] = Field(default=[], description="Optimized daily schedule")
    top_priorities: List[str] = Field(default=[], description="Top priority tasks")
    time_blocks: List[Dict[str, Any]] = Field(default=[], description="Suggested time blocks")
    recommendations: List[str] = Field(default=[], description="Planning recommendations")


class MotivatorOutput(BaseModel):
    """Output from the motivator agent."""
    message: str = Field(..., description="Main motivational message")
    affirmation: Optional[str] = None
    focus_tip: Optional[str] = None
    quote: Optional[str] = None


class WellnessOutput(BaseModel):
    """Output from the wellness agent."""
    break_reminders: List[Dict[str, str]] = Field(default=[], description="Break reminders")
    hydration_reminder: Optional[str] = None
    exercise_suggestion: Optional[str] = None
    mindfulness_tip: Optional[str] = None
    sleep_recommendation: Optional[str] = None


class SummaryOutput(BaseModel):
    """Output from the summary agent."""
    briefing: str = Field(..., description="Complete daily briefing text")
    top_3_priorities: List[str] = Field(default=[], description="Top 3 priorities for the day")
    wellness_highlights: Optional[str] = None
    motivation: Optional[str] = None


class BriefingResponse(BaseModel):
    """Response model for a generated briefing."""
    user_id: str = Field(..., description="User identifier")
    timestamp: str = Field(..., description="Briefing generation timestamp")
    summary: str = Field(..., description="Complete briefing summary")

    # Agent outputs
    planner_output: Dict[str, Any] = Field(default={}, description="Planner agent output")
    motivator_output: Dict[str, Any] = Field(default={}, description="Motivator agent output")
    wellness_output: Dict[str, Any] = Field(default={}, description="Wellness agent output")

    # Optional metadata
    calendar_events: List[CalendarEvent] = Field(default=[], description="Today's calendar events")
    tasks: List[Task] = Field(default=[], description="User's tasks")

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user123",
                "timestamp": "2024-01-15T07:00:00Z",
                "summary": "Good morning! Here's your daily briefing...",
                "planner_output": {
                    "daily_schedule": [],
                    "top_priorities": ["Complete project proposal", "Team meeting"],
                    "time_blocks": []
                },
                "motivator_output": {
                    "message": "You're making great progress on your goals!",
                    "affirmation": "You are capable and prepared."
                },
                "wellness_output": {
                    "break_reminders": [
                        {"time": "10:00 AM", "activity": "5-minute stretch"}
                    ],
                    "hydration_reminder": "Drink water every 2 hours"
                }
            }
        }


class DashboardData(BaseModel):
    """Dashboard data model."""
    user_id: str = Field(..., description="User identifier")
    recent_briefings: List[Dict[str, Any]] = Field(
        default=[],
        description="Recent briefings"
    )
    upcoming_events: List[CalendarEvent] = Field(
        default=[],
        description="Upcoming calendar events"
    )
    user_stats: Dict[str, Any] = Field(
        default={},
        description="User statistics and metrics"
    )
    last_updated: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user123",
                "recent_briefings": [],
                "upcoming_events": [],
                "user_stats": {
                    "briefings_generated": 30,
                    "tasks_completed": 45,
                    "streak_days": 7
                },
                "last_updated": "2024-01-15T07:00:00Z"
            }
        }
