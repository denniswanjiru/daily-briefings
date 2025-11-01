"""
Wellness Agent - Provides health and wellness recommendations.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.language_models import BaseChatModel

from app.core.logger import logger


class WellnessAgent:
    """
    Agent responsible for providing personalized wellness recommendations
    including breaks, exercise, hydration, and mental health tips.
    """

    def __init__(self, llm: BaseChatModel):
        """
        Initialize the Wellness Agent.

        Args:
            llm: Language model instance for generating wellness recommendations
        """
        self.llm = llm
        self.system_prompt = """You are a wellness and health advisor.
Your role is to provide personalized wellness recommendations for the user's day. Consider:
- Scheduled breaks and rest periods
- Physical activity and movement
- Hydration and nutrition reminders
- Stress management techniques
- Sleep and recovery

Recommendations should be practical, evidence-based, and fit into their schedule."""

    async def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate wellness recommendations.

        Args:
            state: Current state with planner output and user preferences

        Returns:
            Updated state with wellness output
        """
        try:
            logger.info("Wellness agent processing...")

            # TODO: Extract relevant context
            # planner_output = state.get("planner_output", {})
            # user_preferences = state.get("user_preferences", {})
            # health_data = state.get("health_data", {})

            # TODO: Build wellness prompt
            # prompt = self._build_prompt(planner_output, user_preferences, health_data)

            # TODO: Call LLM for recommendations
            # messages = [
            #     SystemMessage(content=self.system_prompt),
            #     HumanMessage(content=prompt)
            # ]
            # response = await self.llm.ainvoke(messages)

            # Placeholder response
            wellness = {
                "break_reminders": [
                    {"time": "10:00 AM", "activity": "5-minute stretch"},
                    {"time": "2:00 PM", "activity": "Short walk"}
                ],
                "hydration_reminder": "Drink water every 2 hours",
                "exercise_suggestion": "15-minute evening yoga",
                "mindfulness_tip": "Take 3 deep breaths before each meeting"
            }

            state["wellness_output"] = wellness
            logger.info("Wellness agent completed")

            return state

        except Exception as e:
            logger.error(f"Error in wellness agent: {str(e)}")
            raise

    def _build_prompt(
        self,
        planner_output: Dict[str, Any],
        preferences: Dict[str, Any],
        health_data: Dict[str, Any]
    ) -> str:
        """
        Build the prompt for the wellness LLM.

        Args:
            planner_output: Daily schedule from planner
            preferences: User wellness preferences
            health_data: Any health tracking data

        Returns:
            Formatted prompt string
        """
        # TODO: Implement prompt building logic
        prompt = f"""
        Daily Schedule: {planner_output}
        Preferences: {preferences}
        Health Data: {health_data}

        Please provide wellness recommendations for today.
        """
        return prompt
