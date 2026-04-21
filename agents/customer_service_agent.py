from core.agent import BaseAgent, AgentType, Message
from typing import Dict, Any, List
import logging

class CustomerServiceAgent(BaseAgent):
    """Handles customer inquiries and support requests"""
    
    def __init__(self, agent_id: str = "cs_agent_001"):
        super().__init__(agent_id, AgentType.CUSTOMER_SERVICE, "Customer Service Agent")
        self.capabilities = [
            "answer_general_queries",
            "process_plan_inquiries",
            "handle_service_requests",
            "escalate_to_billing",
            "escalate_to_network"
        ]
        self.logger = logging.getLogger(__name__)
    
    async def process_message(self, message: Message) -> Dict[str, Any]:
        """Process customer service request"""
        self.logger.info(f"Processing message: {message.id}")
        
        request_type = message.content.get("type")
        customer_id = message.content.get("customer_id")
        query = message.content.get("query")
        
        if request_type == "general_query":
            return await self._handle_general_query(customer_id, query)
        elif request_type == "plan_inquiry":
            return await self._handle_plan_inquiry(customer_id, query)
        elif request_type == "service_request":
            return await self._handle_service_request(customer_id, query)
        
        return {"status": "error", "message": "Unknown request type"}
    
    async def _handle_general_query(self, customer_id: str, query: str) -> Dict[str, Any]:
        """Handle general customer query"""
        self.logger.info(f"Handling general query for customer {customer_id}")
        
        responses = {
            "data": "Check your data usage in the app settings or call *123#",
            "balance": "Dial *100# to check your balance",
            "plans": "Visit our website or ask our billing agent for plan details",
            "coverage": "Use our coverage checker tool on the website"
        }
        
        answer = responses.get(query.lower(), "I don't have information about that. Please contact support.")
        
        return {
            "status": "success",
            "customer_id": customer_id,
            "answer": answer,
            "agent_id": self.agent_id
        }
    
    async def _handle_plan_inquiry(self, customer_id: str, query: str) -> Dict[str, Any]:
        """Handle plan inquiry"""
        self.logger.info(f"Handling plan inquiry for customer {customer_id}")
        
        return {
            "status": "success",
            "customer_id": customer_id,
            "message": "Plan details retrieved. Forwarding to billing agent for detailed information.",
            "escalate_to": "billing_agent",
            "agent_id": self.agent_id
        }
    
    async def _handle_service_request(self, customer_id: str, request: str) -> Dict[str, Any]:
        """Handle service request"""
        self.logger.info(f"Handling service request for customer {customer_id}")
        
        return {
            "status": "success",
            "customer_id": customer_id,
            "message": "Service request received and queued.",
            "ticket_id": f"SR-{customer_id}-001",
            "agent_id": self.agent_id
        }
    
    async def get_capabilities(self) -> List[str]:
        """Return capabilities"""
        return self.capabilities
