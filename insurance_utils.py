from typing import Dict, Any
from datetime import datetime, timedelta
import json

class PolicyGenerator:
    def __init__(self):
        self.policy_counter = 0
        
    def generate_policy(self, offer_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generiranje zavarovalne police"""
        self.policy_counter += 1
        
        start_date = datetime.now()
        end_date = start_date + timedelta(days=365)
        
        return {
            "policy_number": f"POL-{datetime.now().year}-{self.policy_counter:04d}",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "premium": offer_data["premium"],
            "coverage": offer_data["coverage"],
            "terms": offer_data["terms"]
        }
    
    def save_policy(self, policy: Dict[str, Any], filepath: str) -> None:
        """Shranjevanje police v JSON formatu"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(policy, f, indent=2, ensure_ascii=False)

class ClaimsHandler:
    def __init__(self):
        self.valid_claim_types = {"damage", "theft", "liability"}
        
    def validate_claim(self, claim_data: Dict[str, Any]) -> bool:
        """Preverjanje veljavnosti zahtevka"""
        return all([
            claim_data.get("type") in self.valid_claim_types,
            claim_data.get("policy_number"),
            claim_data.get("date_of_incident"),
            claim_data.get("description")
        ])
    
    def process_claim(self, claim_data: Dict[str, Any]) -> Dict[str, Any]:
        """Obdelava zahtevka"""
        if not self.validate_claim(claim_data):
            return {"status": "rejected", "reason": "Neveljavni podatki zahtevka"}
            
        # Tukaj bi dodali logiko za oceno zahtevka
        return {
            "status": "processing",
            "claim_id": f"CLM-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "estimated_payout": 0.0
        }