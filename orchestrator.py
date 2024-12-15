from autogen_magentic_one.agents.orchestrator import LedgerOrchestrator
from typing import List
from autogen_core import AgentProxy

class InsuranceOrchestrator(LedgerOrchestrator):
    def __init__(self, agents: List[AgentProxy], **kwargs):
        super().__init__(agents=agents, **kwargs)
        
    async def orchestrate_workflow(self, initial_task: dict):
        """Koordinacija delovnega toka zavarovanja"""
        steps = [
            ("research", "analyze_risk"),
            ("underwriting", "calculate_premium"),
            ("sales", "prepare_offer")
        ]
        
        results = {}
        for agent_name, action in steps:
            agent = self.get_agent(agent_name)
            results[action] = await agent.execute_action(action, initial_task)
            
        return results 