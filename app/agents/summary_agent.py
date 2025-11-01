"""
Summary Agent - Compiles outputs from all agents into a cohesive briefing.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.language_models import BaseChatModel

from app.core.logger import logger


class SummaryAgent:
    """
    Agent responsible for synthesizing outputs from all other agents
    into a coherent, actionable daily briefing.
    """

    def __init__(self, llm: BaseChatModel):
        """
        Initialize the Summary Agent.

        Args:
            llm: Language model instance for generating summary
        """
        self.llm = llm
        self.system_prompt = """You are a skilled executive assistant.
Your role is to compile information from multiple sources into a clear,
concise daily briefing. The briefing should:
- Start with the most important information
- Be scannable and well-organized
- Highlight key actions and priorities
- Integrate planning, motivation, and wellness seamlessly
- Use clear formatting (bullets, sections, etc.)

Keep the tone professional yet friendly."""

    async def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate comprehensive daily briefing summary.

        Args:
            state: Current state with all agent outputs

        Returns:
            Updated state with final summary
        """
        try:
            logger.info("Summary agent processing...")

            # TODO: Extract all agent outputs
            # planner_output = state.get("planner_output", {})
            # motivator_output = state.get("motivator_output", {})
            # wellness_output = state.get("wellness_output", {})

            # TODO: Build summary prompt
            # prompt = self._build_prompt(
            #     planner_output,
            #     motivator_output,
            #     wellness_output
            # )

            # TODO: Call LLM to generate cohesive summary
            # messages = [
            #     SystemMessage(content=self.system_prompt),
            #     HumanMessage(content=prompt)
            # ]
            # response = await self.llm.ainvoke(messages)

            # Placeholder response
            summary = {
                "briefing": "Good morning! Here's your daily briefing...",
                "top_3_priorities": [
                    "Complete project proposal",
                    "Team meeting at 2 PM",
                    "Review client feedback"
                ],
                "wellness_highlights": "Remember to take breaks and stay hydrated",
                "motivation": "You're making great progress on your goals!"
            }

            state["summary_output"] = summary
            logger.info("Summary agent completed")

            return state

        except Exception as e:
            logger.error(f"Error in summary agent: {str(e)}")
            raise

    def _build_prompt(
        self,
        planner_output: Dict[str, Any],
        motivator_output: Dict[str, Any],
        wellness_output: Dict[str, Any]
    ) -> str:
        """
        Build the prompt for the summary LLM.

        Args:
            planner_output: Daily plan from planner agent
            motivator_output: Motivational content
            wellness_output: Wellness recommendations

        Returns:
            Formatted prompt string
        """
        # TODO: Implement prompt building logic
        prompt = f"""
        Daily Plan: {planner_output}
        Motivation: {motivator_output}
        Wellness: {wellness_output}

        Please create a comprehensive daily briefing.
        """
        return prompt
