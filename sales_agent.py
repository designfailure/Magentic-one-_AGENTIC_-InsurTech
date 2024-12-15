from autogen_magentic_one.agents.base import BaseAgent
from typing import Dict, Any

class SalesAgent(BaseAgent):
    def __init__(self, model_client):
        super().__init__(
            name="SalesAgent",
            description="Agent za pripravo ponudbe in komunikacijo s strankami",
            model_client=model_client
        )
        
    async def prepare_offer(self, insurance_data: Dict[str, Any]) -> Dict[str, Any]:
        """Priprava zavarovalne ponudbe"""
        prompt = f"""Pripravi ponudbo za zavarovanje:
        1. Premium: {insurance_data.get('final_premium')}
        2. Kritje: {insurance_data.get('coverage_details')}
        3. Posebni pogoji: {insurance_data.get('special_conditions', [])}
        """
        
        response = await self.model_client.complete(prompt)
        return self._format_offer(response, insurance_data)
    
    def _format_offer(self, offer_text: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Oblikovanje končne ponudbe"""
        return {
            "offer_id": "OFF-" + str(hash(offer_text))[:8],
            "premium": data.get('final_premium'),
            "coverage": data.get('coverage_details'),
            "terms": offer_text,
            "valid_until": "30 days"
        } 