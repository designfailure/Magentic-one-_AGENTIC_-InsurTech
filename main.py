import asyncio
import logging
import os
from autogen_core import EVENT_LOGGER_NAME, AgentId, AgentProxy, SingleThreadedAgentRuntime
from autogen_magentic_one.agents.orchestrator import LedgerOrchestrator
from autogen_magentic_one.utils import LogHandler, create_completion_client_from_env
from agents.research_agent import ResearchAgent
from agents.underwriting_agent import UnderwritingAgent
from agents.sales_agent import SalesAgent
from runtime.orchestrator import InsuranceOrchestrator

async def main(logs_dir: str) -> None:
    # Ustvarimo runtime
    runtime = SingleThreadedAgentRuntime()
    
    # Ustvarimo client za LLM
    client = create_completion_client_from_env(model="gpt-4")
    
    # Registriramo agente
    await ResearchAgent.register(runtime, "ResearchAgent", 
                               lambda: ResearchAgent(model_client=client))
    research = AgentProxy(AgentId("ResearchAgent", "default"), runtime)
    
    await UnderwritingAgent.register(runtime, "UnderwritingAgent",
                                   lambda: UnderwritingAgent(model_client=client))
    underwriting = AgentProxy(AgentId("UnderwritingAgent", "default"), runtime)
    
    await SalesAgent.register(runtime, "SalesAgent",
                            lambda: SalesAgent(model_client=client))
    sales = AgentProxy(AgentId("SalesAgent", "default"), runtime)
    
    agent_list = [research, underwriting, sales]
    
    # Registriramo orchestrator
    await InsuranceOrchestrator.register(
        runtime,
        "Orchestrator",
        lambda: InsuranceOrchestrator(
            agents=agent_list,
            model_client=client,
            max_rounds=30,
            max_time=25 * 60,
            return_final_answer=True,
        )
    )
    
    runtime.start()
    await runtime.stop_when_idle()

if __name__ == "__main__":
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        
    logger = logging.getLogger(EVENT_LOGGER_NAME)
    logger.setLevel(logging.INFO)
    log_handler = LogHandler(filename=os.path.join(logs_dir, "insurance_log.jsonl"))
    logger.handlers = [log_handler]
    
    asyncio.run(main(logs_dir)) 