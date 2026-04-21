from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

class AgentType(Enum):
    TYPE_A = "Type A"
    TYPE_B = "Type B"
    TYPE_C = "Type C"

@dataclass
class Message:
    sender: str
    receiver: str
    content: str
    timestamp: str

class BaseAgent(ABC):
    @abstractmethod
    def send_message(self, message: Message):
        pass

    @abstractmethod
    def receive_message(self) -> Message:
        pass
