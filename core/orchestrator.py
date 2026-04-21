from typing import Dict, List, Optional, Any
import logging

class AgentOrchestrator:
    """Orchestrates communication and task delegation between agents"""
    
    def __init__(self):
        self.agents: Dict[str, any] = {}
        self.message_history: List[Dict] = []
        self.logger = logging.getLogger(__name__)
    
    def register_agent(self, agent_id: str, agent: Any) -> bool:
        """Register an agent with the orchestrator"""
        if agent_id in self.agents:
            self.logger.warning(f"Agent {agent_id} already registered")
            return False
        
        self.agents[agent_id] = agent
        self.logger.info(f"Agent {agent_id} registered successfully")
        return True
    
    def deregister_agent(self, agent_id: str) -> bool:
        """Deregister an agent"""
        if agent_id not in self.agents:
            return False
        
        del self.agents[agent_id]
        self.logger.info(f"Agent {agent_id} deregistered")
        return True
    
    def route_message(self, message: Dict[str, Any]) -> bool:
        """Route message to appropriate agent"""
        receiver_id = message.get("receiver_id")
        
        if receiver_id not in self.agents:
            self.logger.error(f"Receiver {receiver_id} not found")
            return False
        
        self.message_history.append(message)
        self.logger.info(f"Message routed to {receiver_id}")
        return True
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get system status"""
        return {
            "total_agents": len(self.agents),
            "message_history_size": len(self.message_history),
            "agents": list(self.agents.keys())
        }