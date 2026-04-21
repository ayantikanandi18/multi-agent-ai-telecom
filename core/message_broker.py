import asyncio
from typing import Callable, Dict, List, Any
from core.agent import Message
import logging

class MessageBroker:
    """Message broker for handling inter-agent communication"""
    
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}
        self.message_queue: asyncio.Queue = asyncio.Queue()
        self.logger = logging.getLogger(__name__)
    
    async def subscribe(self, topic: str, callback: Callable) -> str:
        """Subscribe to a topic"""
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        
        self.subscribers[topic].append(callback)
        self.logger.info(f"Subscribed to topic: {topic}")
        return topic
    
    async def unsubscribe(self, topic: str, callback: Callable) -> bool:
        """Unsubscribe from a topic"""
        if topic not in self.subscribers:
            return False
        
        if callback in self.subscribers[topic]:
            self.subscribers[topic].remove(callback)
            return True
        
        return False
    
    async def publish(self, topic: str, message: Dict[str, Any]) -> None:
        """Publish message to a topic"""
        await self.message_queue.put({"topic": topic, "message": message})
        self.logger.info(f"Message published to topic: {topic}")
    
    async def process_messages(self) -> None:
        """Process published messages"""
        while True:
            try:
                data = await asyncio.wait_for(self.message_queue.get(), timeout=5.0)
                topic = data["topic"]
                message = data["message"]
                
                if topic in self.subscribers:
                    tasks = [callback(message) for callback in self.subscribers[topic]]
                    await asyncio.gather(*tasks)
            
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                self.logger.error(f"Error processing message: {str(e)}")
