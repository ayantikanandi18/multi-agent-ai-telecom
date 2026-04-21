from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
import uuid
from typing import Dict, Any, List

class AgentType(Enum):
    CUSTOMER_SERVICE = "customer_service"
    BILLING = "billing"
    NETWORK_MONITORING = "network_monitoring"
    COMPLAINT_RESOLUTION = "complaint_resolution"
    PREDICTIVE_MAINTENANCE = "predictive_maintenance"

@dataclass
class Message:
    id: str
    sender_id: str
    receiver_id: str
    content: Dict[str, Any]
    timestamp: datetime
    priority: int = 0
    
    def __init__(self, sender_id: str, receiver_id: str, content: Dict[str, Any], priority: int = 0):
        self.id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = datetime.utcnow()
        self.priority = priority

class BaseAgent(ABC):
    """Base class for all telecom agents"""
    
    def __init__(self, agent_id: str, agent_type: AgentType, name: str):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.name = name
        self.message_queue: List[Message] = []
        self.capabilities: List[str] = []
        self.is_active = True
        
    @abstractmethod
    def process_message(self, message: Message) -> Dict[str, Any]:
        """Process incoming message and return response"""
        pass
    
    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """Return list of capabilities this agent can perform"""
        pass
    
    def send_message(self, receiver_id: str, content: Dict[str, Any], priority: int = 0) -> Message:
        """Send message to another agent"""
        message = Message(self.agent_id, receiver_id, content, priority)
        return message
    
    def receive_message(self, message: Message) -> None:
        """Receive message and add to queue"""
        self.message_queue.append(message)
    
    def process_queue(self) -> None:
        """Process all messages in queue"""
        while self.message_queue:
            message = self.message_queue.pop(0)
            self.process_message(message)
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "type": self.agent_type.value,
            "is_active": self.is_active,
            "queue_size": len(self.message_queue),
            "capabilities": self.capabilities
        }