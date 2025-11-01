"""
Motivator Agent - Provides encouragement and motivation.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.language_models import BaseChatModel

from app.core.logger import logger


class MotivatorAgent:
    """
    Agent responsible for generating personalized motivational content
    based on user's goals, progress, and current context.
    """

    def __init__(self, llm: BaseChatModel):
        """
        Initialize the Motivator Agent.

        Args:
            llm: Language model instance for generating motivational content
        """
        self.llm = llm
        self.system_prompt = """You are an empathetic and encouraging motivational coach.
Your role is to inspire and energize the user for their day ahead. Consider:
- Their current goals and progress
- Recent achievements (celebrate wins!)
- Upcoming challenges
- Personal preferences and what motivates them
- Tone should be positive, authentic, and personalized

Keep messages concise and actionable."""

    async def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate motivational content for the user.

        Args:
            state: Current state with user context and planner output

        Returns:
            Updated state with motivator output
        """
        try:
            logger.info("Motivator agent processing...")

            # TODO: Extract relevant context from state
            # planner_output = state.get("planner_output", {})
            # user_goals = state.get("user_goals", [])
            # recent_achievements = state.get("achievements", [])

            # TODO: Build motivational prompt
            # prompt = self._build_prompt(planner_output, user_goals, recent_achievements)

            # TODO: Call LLM to generate motivation
            # messages = [
            #     SystemMessage(content=self.system_prompt),
            #     HumanMessage(content=prompt)
            # ]
            # response = await self.llm.ainvoke(messages)

            # Placeholder response
            motivation = {
                "message": "You've got this! Focus on your top priorities today.",
                "affirmation": "You are capable and prepared.",
                "focus_tip": "Start with your most important task."
            }

            state["motivator_output"] = motivation
            logger.info("Motivator agent completed")

            return state

        except Exception as e:
            logger.error(f"Error in motivator agent: {str(e)}")
            raise

    def _build_prompt(
        self,
        planner_output: Dict[str, Any],
        goals: list,
        achievements: list
    ) -> str:
        """
        Build the prompt for the motivator LLM.

        Args:
            planner_output: Output from planner agent
            goals: User's current goals
            achievements: Recent achievements

        Returns:
            Formatted prompt string
        """
        # TODO: Implement prompt building logic
        prompt = f"""
        Today's Plan: {planner_output}
        Goals: {goals}
        Recent Achievements: {achievements}

        Please create a motivational message for the user.
        """
        return prompt
