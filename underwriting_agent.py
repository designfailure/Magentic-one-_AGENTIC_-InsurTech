from autogen_magentic_one.agents.base import BaseAgent
from typing import Dict, Any

class UnderwritingAgent(BaseAgent):
    def __init__(self, model_client):
        super().__init__(
            name="UnderwritingAgent",
            description="Agent za oceno tveganja in izračun premije",
            model_client=model_client
        )
        
    async def calculate_premium(self, risk_data: Dict[str, Any]) -> Dict[str, Any]:
        """Izračun zavarovalne premije na podlagi ocene tveganja"""
        prompt = f"""Oceni tveganje in izračunaj premijo za:
        1. Identificirani objekti: {risk_data.get('objects', [])}
        2. Dejavniki tveganja: {risk_data.get('risk_factors', [])}
        3. Lokacija: {risk_data.get('location', 'Unknown')}
        """
        
        response = await self.model_client.complete(prompt)
        return self._calculate_final_premium(response)
    
    def _calculate_final_premium(self, assessment: str) -> Dict[str, Any]:
        """Izračun končne premije na podlagi ocene"""
        return {
            "base_premium": 0.0,
            "risk_multiplier": 1.0,
            "final_premium": 0.0,
            "coverage_details": {}
        } 