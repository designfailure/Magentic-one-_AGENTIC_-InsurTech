from magentic import Agent, prompt
from tools import ImageCaptioning, WebSearch, GoogleSheets

class ResearchAgent(Agent):
    def __init__(self, name: str, description: str):
        super().__init__(name=name, description=description)
        self.tools = {
            "image_caption": ImageCaptioning(),
            "web_search": WebSearch(),
            "sheets": GoogleSheets()
        }
    
    @prompt("Analiziraj sliko in identificiraj objekte ter dejavnike tveganja")
    async def process_image(self, image):
        """Obdelava slike z uporabo magentic-one promptov"""
        return await self.tools["image_caption"].analyze(image)

class UnderwritingAgent(Agent):
    def __init__(self, name: str, description: str):
        super().__init__(name=name, description=description)
    
    @prompt("Oceni tveganje in določi ustrezno kritje")
    async def assess_risk(self, data):
        """Ocena tveganja z uporabo magentic-one promptov"""
        # Implementacija ocene tveganja
        pass

# Podobno implementirajte še SalesAgent in DelegationAgent